from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from .models import Producto

CLAVE = "Clave-De-Prueba-123"


def datos(**cambios):
    base = {
        "nombre": "Cuaderno",
        "descripcion": "Cuaderno universitario",
        "precio": "19.99",
        "stock": "50",
    }
    base.update(cambios)
    return base


class BaseAcceso(TestCase):
    """Cuentas ficticias: dos usuarios normales y un miembro del personal."""

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.ana = User.objects.create_user("ana", password=CLAVE)
        cls.beto = User.objects.create_user("beto", password=CLAVE)
        cls.staff = User.objects.create_user("jefa", password=CLAVE, is_staff=True)
        cls.p_ana = Producto.objects.create(
            nombre="De Ana", descripcion="x", precio=Decimal("10"),
            stock=5, costo_interno=Decimal("4.50"), propietario=cls.ana,
        )
        cls.p_beto = Producto.objects.create(
            nombre="De Beto", descripcion="x", precio=Decimal("20"),
            stock=7, costo_interno=Decimal("9.00"), propietario=cls.beto,
        )

    def entrar(self, usuario):
        self.client.force_login(usuario)


class AutenticacionTests(BaseAcceso):
    def test_anonimo_no_accede_a_rutas_privadas(self):
        rutas = [
            reverse("producto-list"),
            reverse("producto-create"),
            reverse("producto-detail", args=[self.p_ana.pk]),
            reverse("producto-update", args=[self.p_ana.pk]),
            reverse("producto-delete", args=[self.p_ana.pk]),
        ]
        for ruta in rutas:
            resp = self.client.get(ruta, secure=True)
            self.assertEqual(resp.status_code, 302, ruta)
            self.assertIn(reverse("login"), resp["Location"], ruta)

    def test_anonimo_no_puede_escribir(self):
        total = Producto.objects.count()
        self.client.post(reverse("producto-create"), datos(), secure=True)
        self.client.post(reverse("producto-update", args=[self.p_ana.pk]),
                         datos(nombre="Hackeado"), secure=True)
        self.client.post(reverse("producto-delete", args=[self.p_ana.pk]), secure=True)
        self.assertEqual(Producto.objects.count(), total)
        self.p_ana.refresh_from_db()
        self.assertEqual(self.p_ana.nombre, "De Ana")

    def test_login_con_credenciales_validas(self):
        resp = self.client.post(
            reverse("login"), {"username": "ana", "password": CLAVE}, secure=True)
        self.assertRedirects(resp, reverse("producto-list"),
                             fetch_redirect_response=False)
        self.assertIn("_auth_user_id", self.client.session)

    def test_login_con_credenciales_invalidas(self):
        resp = self.client.post(
            reverse("login"), {"username": "ana", "password": "incorrecta"}, secure=True)
        self.assertEqual(resp.status_code, 200)
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_logout_por_get_no_cierra_sesion(self):
        self.entrar(self.ana)
        resp = self.client.get(reverse("logout"), secure=True)
        self.assertEqual(resp.status_code, 405)
        self.assertIn("_auth_user_id", self.client.session)

    def test_logout_por_post_cierra_sesion(self):
        self.entrar(self.ana)
        resp = self.client.post(reverse("logout"), secure=True)
        self.assertRedirects(resp, reverse("login"), fetch_redirect_response=False)
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_logout_sin_token_csrf_se_rechaza(self):
        # Se envia un Referer valido para que el rechazo se deba solo al token faltante.
        cliente = Client(enforce_csrf_checks=True)
        cliente.force_login(self.ana)
        resp = cliente.post(reverse("logout"), secure=True,
                            headers={"referer": "https://testserver/"})
        self.assertEqual(resp.status_code, 403)
        self.assertIn("_auth_user_id", cliente.session)

    def test_boton_de_logout_es_un_formulario_post_con_csrf(self):
        self.entrar(self.ana)
        html = self.client.get(reverse("producto-list"), secure=True).content.decode()
        self.assertIn('method="post" action="%s"' % reverse("logout"), html)
        self.assertIn("csrfmiddlewaretoken", html)


class AutorizacionPorRegistroTests(BaseAcceso):
    def test_listado_solo_muestra_registros_propios(self):
        self.entrar(self.ana)
        resp = self.client.get(reverse("producto-list"), secure=True)
        self.assertContains(resp, "De Ana")
        self.assertNotContains(resp, "De Beto")

    def test_ver_producto_ajeno_responde_404(self):
        self.entrar(self.ana)
        resp = self.client.get(reverse("producto-detail", args=[self.p_beto.pk]), secure=True)
        self.assertEqual(resp.status_code, 404)

    def test_editar_producto_ajeno_responde_404_y_no_cambia(self):
        self.entrar(self.ana)
        url = reverse("producto-update", args=[self.p_beto.pk])
        self.assertEqual(self.client.get(url, secure=True).status_code, 404)
        resp = self.client.post(url, datos(nombre="Robado"), secure=True)
        self.assertEqual(resp.status_code, 404)
        self.p_beto.refresh_from_db()
        self.assertEqual(self.p_beto.nombre, "De Beto")

    def test_eliminar_producto_ajeno_responde_404_y_no_borra(self):
        self.entrar(self.ana)
        url = reverse("producto-delete", args=[self.p_beto.pk])
        self.assertEqual(self.client.get(url, secure=True).status_code, 404)
        self.assertEqual(self.client.post(url, secure=True).status_code, 404)
        self.assertTrue(Producto.objects.filter(pk=self.p_beto.pk).exists())

    def test_usuario_edita_y_elimina_sus_propios_registros(self):
        self.entrar(self.ana)
        resp = self.client.post(reverse("producto-update", args=[self.p_ana.pk]),
                                datos(nombre="Editado por Ana"), secure=True)
        self.assertEqual(resp.status_code, 302)
        self.p_ana.refresh_from_db()
        self.assertEqual(self.p_ana.nombre, "Editado por Ana")
        resp = self.client.post(reverse("producto-delete", args=[self.p_ana.pk]), secure=True)
        self.assertEqual(resp.status_code, 302)
        self.assertFalse(Producto.objects.filter(pk=self.p_ana.pk).exists())

    def test_crear_asigna_propietario_desde_la_sesion(self):
        self.entrar(self.ana)
        self.client.post(reverse("producto-create"),
                         datos(nombre="Nuevo", propietario=self.beto.pk), secure=True)
        nuevo = Producto.objects.get(nombre="Nuevo")
        self.assertEqual(nuevo.propietario, self.ana)  # el POST manipulado se ignora

    def test_personal_ve_y_administra_todos_los_registros(self):
        self.entrar(self.staff)
        resp = self.client.get(reverse("producto-list"), secure=True)
        self.assertContains(resp, "De Ana")
        self.assertContains(resp, "De Beto")
        resp = self.client.post(reverse("producto-delete", args=[self.p_beto.pk]), secure=True)
        self.assertEqual(resp.status_code, 302)
        self.assertFalse(Producto.objects.filter(pk=self.p_beto.pk).exists())


class MinimizacionCostoInternoTests(BaseAcceso):
    def test_usuario_normal_no_ve_el_costo_interno(self):
        self.entrar(self.ana)
        for url in (reverse("producto-list"),
                    reverse("producto-detail", args=[self.p_ana.pk])):
            html = self.client.get(url, secure=True).content.decode()
            self.assertNotIn("Costo interno", html)
            self.assertNotIn("4.50", html)

    def test_usuario_normal_no_puede_modificar_el_costo_con_un_post_manipulado(self):
        self.entrar(self.ana)
        self.client.post(reverse("producto-update", args=[self.p_ana.pk]),
                         datos(costo_interno="0.01"), secure=True)
        self.p_ana.refresh_from_db()
        self.assertEqual(self.p_ana.costo_interno, Decimal("4.50"))

    def test_personal_ve_el_costo_interno(self):
        self.entrar(self.staff)
        html = self.client.get(
            reverse("producto-detail", args=[self.p_ana.pk]), secure=True).content.decode()
        self.assertIn("Costo interno", html)
        self.assertIn("4.50", html)
