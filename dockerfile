FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia todo el contenido del proyecto al contenedor
COPY . .

# Instala el proyecto como paquete en modo editable
RUN pip install -e .

# Establece el path para que Python encuentre los módulos correctamente
ENV PYTHONPATH=/app/src

# Ejecuta el archivo principal como módulo (recomendado)
CMD ["python", "-m", "edu_pad.main"]