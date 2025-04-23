import os
import pandas as pd
import mlflow
import mlflow.sklearn
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from dotenv import load_dotenv
import time

load_dotenv()

def wait_for_db():
    while True:
        try:
            time.sleep(20)
            engine.connect()
            print("✅ Connexion à la base de données réussie.")
            break
        except OperationalError:
            print("⏳ Attente de la base de données...")
            time.sleep(5)

# Connexion à la base
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST")
port = 5432
dbname = os.getenv("POSTGRES_DB")

engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')

wait_for_db()

df = pd.read_sql("SELECT * FROM iris_data", engine)

X = df[['sepal_width']]
y = df['sepal_length']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modèle
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
rmse = mean_squared_error(y_test, y_pred, squared=False)

print(f"✅ RMSE: {rmse}")

# MLflow
mlflow.set_tracking_uri("http://mlflow:5000")
mlflow.set_experiment("iris_regression")

with mlflow.start_run():
    mlflow.log_param("model", "RandomForest")
    mlflow.log_metric("rmse", rmse)
    mlflow.sklearn.log_model(model, "model")

print("✅ Modèle enregistré avec MLflow")
