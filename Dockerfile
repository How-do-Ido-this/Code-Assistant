# Dockerfile
# Usamos una imagen de Python oficial, pequeña y optimizada
FROM python:3.14-slim

# Definimos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos primero solo el archivo de requerimientos para aprovechar el caché de Docker
# Esto hace que las instalaciones posteriores sean más rápidas
COPY requirements.txt .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código fuente al directorio de trabajo
COPY . .

# Exponemos el puerto que usa FastAPI
EXPOSE 8000

# Comando para arrancar la API con Uvicorn
# --host 0.0.0.0 es necesario para que el servidor sea accesible desde fuera del contenedor
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
