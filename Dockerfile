# Imagen oficial de Python compatible con Django 6.1 (requiere Python 3.12 o superior)
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Usuario sin privilegios y carpeta /data para la base SQLite (volumen).
RUN useradd --system --create-home app \
    && mkdir /data \
    && chown app:app /data \
    && SECRET_KEY=valor-solo-para-el-build USAR_WHITENOISE=True \
       python manage.py collectstatic --noinput
USER app

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/login/')"

# Aplica migraciones y arranca gunicorn (sin runserver, que es solo para desarrollo).
CMD ["sh", "-c", "python manage.py migrate --noinput && gunicorn crud_django.wsgi:application --bind 0.0.0.0:8000 --workers 2"]
