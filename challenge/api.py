import fastapi
import pandas as pd
from fastapi import HTTPException
from typing import List

# Importar la clase DelayModel que definimos previamente
from model import DelayModel

# Crear una instancia de FastAPI
app = fastapi.FastAPI()

# Crear una instancia de la clase DelayModel
model = DelayModel()

# Cargar los datos desde el archivo CSV
data = pd.read_csv('../data/data.csv')

# Ruta para verificar la salud de la API
@app.get("/health", status_code=200)
async def get_health() -> dict:
    return {
        "status": "OK"
    }

# Ruta para entrenar el modelo
@app.post("/train", status_code=200)
async def post_train() -> dict:
    try:
        # Preprocesar los datos para entrenamiento
        features, target = model.preprocess(data, target_column='delay')

        # Entrenar el modelo
        model.fit(features, target)

        return {
            "message": "Model trained successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Ruta para realizar predicciones de retraso de vuelo
@app.post("/predict", status_code=200)
async def post_predict(features: List[dict]) -> dict:
    try:
        # Crear un DataFrame a partir de los datos de entrada
        input_data = pd.DataFrame(features)

        # Preprocesar los datos
        preprocessed_data = model.preprocess(input_data)

        # Realizar predicciones
        predictions = model.predict(preprocessed_data)

        # Devolver las predicciones como respuesta
        return {
            "predictions": predictions.tolist()
        }
    except Exception as e:
        # Manejar cualquier error y devolver una respuesta de error
        raise HTTPException(status_code=500, detail=str(e))
