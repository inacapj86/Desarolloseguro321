from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import TestCase

from .models import Producto


class CrearDatosDemoTests(TestCase):
    def test_crea_cuentas_con_los_roles_esperados(self):
        call_command("crear_datos_demo", clave="Clave-Solo-Para-Tests-987", verbosity=0)
        User = get_user_model()
        self.assertFalse(User.objects.get(username="ana").is_staff)
        self.assertFalse(User.objects.get(username="beto").is_staff)
        self.assertTrue(User.objects.get(username="jefa").is_staff)
        self.assertEqual(Producto.objects.count(), 2)

    def test_es_idempotente(self):
        for _ in range(2):
            call_command("crear_datos_demo", clave="Clave-Solo-Para-Tests-987", verbosity=0)
        self.assertEqual(get_user_model().objects.count(), 3)
        self.assertEqual(Producto.objects.count(), 2)

    def test_rechaza_una_clave_debil(self):
        with self.assertRaises(CommandError):
            call_command("crear_datos_demo", clave="123", verbosity=0)
        self.assertEqual(get_user_model().objects.count(), 0)
