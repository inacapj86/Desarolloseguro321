import re

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from .models import Producto

CLAVE = "Clave-De-Prueba-123"
CARGA_XSS = '"><script>alert(1)</script>'


class EndurecimientoTests(TestCase):
    """Verifica las correcciones motivadas por el analisis inicial de ZAP."""

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.ana = User.objects.create_user("ana", password=CLAVE)
        cls.producto = Producto.objects.create(
            nombre="De Ana", descripcion="x", precio=10, stock=5, propietario=cls.ana)

    # --- ZAP 10038: Content Security Policy ---
    def test_politica_csp_estricta_en_login_y_paginas_privadas(self):
        self.client.force_login(self.ana)
        for url in (reverse("login"), reverse("producto-list"),
                    reverse("producto-detail", args=[self.producto.pk])):
            csp = self.client.get(url, secure=True).headers.get("Content-Security-Policy", "")
            self.assertIn("default-src 'self'", csp, url)
            self.assertIn("frame-ancestors 'none'", csp, url)
            self.assertIn("object-src 'none'", csp, url)
            self.assertNotIn("unsafe-inline", csp, url)

    # --- Hallazgo manual: paginas privadas sin Cache-Control ---
    def test_paginas_privadas_no_se_guardan_en_cache(self):
        self.client.force_login(self.ana)
        pk = self.producto.pk
        rutas = [reverse("producto-list"), reverse("producto-create"),
                 reverse("producto-detail", args=[pk]),
                 reverse("producto-update", args=[pk]),
                 reverse("producto-delete", args=[pk])]
        for url in rutas:
            cache = self.client.get(url, secure=True).headers.get("Cache-Control", "")
            self.assertIn("no-store", cache, url)
            self.assertIn("private", cache, url)

    def test_redireccion_al_login_tampoco_se_guarda_en_cache(self):
        resp = self.client.get(reverse("producto-list"), secure=True)
        self.assertEqual(resp.status_code, 302)
        self.assertIn("no-store", resp.headers.get("Cache-Control", ""))

    # --- ZAP 10010: cookie del token CSRF sin HttpOnly ---
    def test_cookie_csrf_es_httponly(self):
        self.client.get(reverse("login"), secure=True)
        self.assertTrue(self.client.cookies["csrftoken"]["httponly"])

    def test_login_sigue_funcionando_con_la_cookie_httponly(self):
        cliente = Client(enforce_csrf_checks=True)
        html = cliente.get(reverse("login"), secure=True).content.decode()
        token = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', html).group(1)
        resp = cliente.post(reverse("login"), {
            "username": "ana", "password": CLAVE, "csrfmiddlewaretoken": token},
            secure=True, headers={"referer": "https://testserver/login/"})
        self.assertEqual(resp.status_code, 302)
        self.assertIn("_auth_user_id", cliente.session)

    # --- ZAP 10031: atributo HTML controlable por el usuario ---
    def test_formulario_escapa_la_entrada_del_usuario_en_los_atributos(self):
        self.client.force_login(self.ana)
        resp = self.client.post(reverse("producto-create"), {
            "nombre": CARGA_XSS, "descripcion": CARGA_XSS,
            "precio": "no-es-numero", "stock": "5"}, secure=True)
        html = resp.content.decode()
        self.assertEqual(resp.status_code, 200)  # el formulario se vuelve a mostrar
        self.assertNotIn("<script>alert(1)</script>", html)
        self.assertIn("&lt;script&gt;alert(1)&lt;/script&gt;", html)
