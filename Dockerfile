# Usa la imagen base de Python 3.11.4
FROM python:3.11.4

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido del directorio actual al directorio de trabajo
COPY . .

# Comando para ejecutar tu aplicación
CMD [ "python", "chagenlle/api.py" ]
