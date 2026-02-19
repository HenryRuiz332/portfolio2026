# Usa la versión más reciente y estable de Python
FROM python:3.13-slim

# Evita que Python genere archivos .pyc y permite logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo
WORKDIR /app

# Instalamos dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalamos dependencias de Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código
COPY . /app/

# Exponemos el puerto de Django
EXPOSE 8000

# Comando por defecto para desarrollo
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]