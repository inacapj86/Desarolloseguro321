from django.test import TestCase
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .forms import ProductoForm
from .models import Producto


def datos(**cambios):
    base = {
        "nombre": "Cuaderno",
        "descripcion": "Cuaderno universitario",
        "precio": "19.99",
        "stock": "50",
    }
    base.update(cambios)
    return base


class ValidacionStockTests(TestCase):
    def test_stock_valido_dentro_del_rango(self):
        self.assertTrue(ProductoForm(datos(stock="50")).is_valid())

    def test_stock_bajo_el_minimo_se_rechaza(self):
        form = ProductoForm(datos(stock="-1"))
        self.assertFalse(form.is_valid())
        self.assertIn("stock", form.errors)

    def test_stock_en_el_minimo_exacto_se_acepta(self):
        self.assertTrue(ProductoForm(datos(stock="0")).is_valid())


class ValidacionPrecioTests(TestCase):
    def test_precio_valido(self):
        self.assertTrue(ProductoForm(datos(precio="19.99")).is_valid())

    def test_precio_negativo_se_rechaza(self):
        form = ProductoForm(datos(precio="-5.00"))
        self.assertFalse(form.is_valid())
        self.assertIn("precio", form.errors)

    def test_precio_en_el_minimo_exacto_se_acepta(self):
        self.assertTrue(ProductoForm(datos(precio="0.01")).is_valid())


class BackendSinNavegadorTests(TestCase):
    """POST directo a la vista: no depende de ninguna restriccion HTML/JS."""

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user("tester", password="Clave-De-Prueba-123")
        self.client.force_login(self.user)

    def test_vista_no_guarda_stock_negativo(self):
        resp = self.client.post(reverse("producto-create"), datos(stock="-1"), secure=True)
        self.assertEqual(resp.status_code, 200)  # vuelve al formulario con errores
        self.assertEqual(Producto.objects.count(), 0)

    def test_vista_guarda_datos_validos(self):
        resp = self.client.post(reverse("producto-create"), datos(), secure=True)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Producto.objects.get().precio, Decimal("19.99"))
# Create your tests here.
