# CRUD Django seguro (laboratorio Docker)

CRUD de productos en Django con login, permisos por registro y ejecucion en Docker.
Proyecto de la asignatura Desarrollo Seguro (Inacap). **Solo para laboratorio local, con datos y cuentas ficticias.**

## Requisitos
- Docker Desktop con Docker Compose v2 (`docker --version`, `docker compose version`)
- Python 3.12 o superior en el equipo (solo para generar la clave y correr los tests fuera de Docker)
- OWASP ZAP Desktop en el equipo anfitrion (para la etapa de analisis)

## Puesta en marcha
1. Copia la configuracion de ejemplo y edita los valores:
   ```
   copy .env.example .env
   python -c "import secrets; print(secrets.token_urlsafe(50))"
   ```
   Pega la clave generada en `SECRET_KEY` dentro de `.env`. El archivo `.env` esta en `.gitignore`: nunca se sube.
2. Construye y levanta el servicio:
   ```
   docker compose up --build -d
   docker compose ps
   ```
   Las migraciones se aplican solas al arrancar el contenedor.
3. Crea las cuentas de prueba (ficticias) con una clave que elijas:
   ```
   docker compose exec web python manage.py crear_datos_demo --clave "TuClaveDePrueba-123"
   ```
   - `ana` y `beto`: usuarios normales (ven y editan solo sus productos)
   - `jefa`: personal (`is_staff`; ve todos los productos, el costo interno y el propietario)
4. Abre http://127.0.0.1:8000 e inicia sesion.

## URL y puertos
- Aplicacion: http://127.0.0.1:8000 (el puerto se publica solo en la interfaz local)
- Objetivo de ZAP Desktop: http://127.0.0.1:8000

## Pruebas
```
python manage.py test -v 2                      # en el equipo
docker compose exec web python manage.py test   # dentro del contenedor
```

## Perfil de laboratorio vs. despliegue real
El `.env.example` desactiva `SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE` y HSTS
porque el laboratorio usa http. Por defecto el proyecto los deja activados; en un despliegue con HTTPS
no deben cambiarse. `DEBUG=False`, `ALLOWED_HOSTS` acotado y los secretos por variables de entorno
se mantienen en ambos casos.

## Comandos utiles
```
docker compose logs -f web      # ver registros
docker compose down             # detener (conserva la base)
docker compose down -v          # detener y borrar la base de datos de prueba
```

## Archivos de la imagen
- `Dockerfile`: imagen `python:3.13-slim`, dependencias desde `requirements.txt`, usuario sin privilegios, gunicorn.
- `compose.yaml`: servicio `web`, puerto `127.0.0.1:8000`, volumen `db_data` para SQLite.
- `.dockerignore` y `.gitignore`: excluyen entornos virtuales, secretos y bases de datos.
