FROM python:3.11.4

WORKDIR /app

COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido del directorio actual al directorio de trabajo
COPY . .

# Comando para ejecutar tu aplicación
CMD [ "python", "chagenlle/api.py" ]
