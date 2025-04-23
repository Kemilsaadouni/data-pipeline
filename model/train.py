import os
import pandas as pd
import mlflow
import mlflow.sklearn
from sqlalchemy import create_engine
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from dotenv import load_dotenv

load_dotenv()

# Connexion à la base
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST")
port = 5432
dbname = os.getenv("POSTGRES_DB")

engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')

# Chargement des données
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
