from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandError

from productos.models import Producto


class Command(BaseCommand):
    help = (
        "Crea cuentas y productos FICTICIOS para el laboratorio: "
        "ana y beto (usuarios normales) y jefa (personal). No usar en produccion."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--clave", required=True,
            help="Clave para las tres cuentas de prueba (no se guarda en el repositorio).",
        )

    def handle(self, *args, **opciones):
        clave = opciones["clave"]
        try:
            validate_password(clave)
        except ValidationError as error:
            raise CommandError("Clave rechazada: " + " ".join(error.messages))

        User = get_user_model()
        cuentas = {}
        for nombre, es_personal in (("ana", False), ("beto", False), ("jefa", True)):
            usuario, _ = User.objects.get_or_create(username=nombre)
            usuario.is_staff = es_personal
            usuario.set_password(clave)
            usuario.save()
            cuentas[nombre] = usuario

        for dueno, nombre, precio, costo in (
            ("ana", "Producto de Ana", 15, 6),
            ("beto", "Producto de Beto", 10, 4),
        ):
            Producto.objects.get_or_create(
                nombre=nombre,
                defaults={
                    "descripcion": "Dato ficticio de laboratorio",
                    "precio": precio,
                    "stock": 5,
                    "costo_interno": costo,
                    "propietario": cuentas[dueno],
                },
            )

        self.stdout.write(self.style.SUCCESS(
            "Cuentas listas: ana y beto (normales), jefa (personal)."))
