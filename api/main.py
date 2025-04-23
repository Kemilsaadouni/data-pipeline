from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.pyfunc
import os
import time


time.sleep(50)
# Définition de l'input attendu
class InputData(BaseModel):
    sepal_width: float

app = FastAPI()

# Lecture du chemin du dernier modèle enregistré
MODEL_PATH_FILE = "/shared/last_model_path.txt"

if not os.path.exists(MODEL_PATH_FILE):
    raise FileNotFoundError(f"Fichier {MODEL_PATH_FILE} introuvable. Assure-toi d’avoir entraîné un modèle avant de lancer l’API.")

with open(MODEL_PATH_FILE, "r") as f:
    model_path = f.read().strip()

# Chargement du modèle
model = mlflow.pyfunc.load_model(model_path)

@app.get("/")
def root():
    return {"message": "✅ API Iris prête !"}

@app.post("/predict")
def predict(input_data: InputData):
    prediction = model.predict([[input_data.sepal_width]])
    return {"predicted_sepal_length": float(prediction[0])}
