import os
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import time
from dotenv import load_dotenv

# Charge les variables d'environnement depuis le fichier .env
load_dotenv()

user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST")
port = 5432
dbname = os.getenv("POSTGRES_DB")

time.sleep(10)
df = pd.read_csv('/data/iris.csv')

# Nettoyage des noms de colonnes (Standardisation)
df.columns = [col.strip().lower().replace('.', '_') for col in df.columns]

# Suppression des valeurs manquantes et des doublons
if df.isnull().sum().sum() > 0:
    print("⚠️ Données manquantes détectées, suppression en cours...")
    df.dropna(inplace=True)

initial_len = len(df)
df.drop_duplicates(inplace=True)
if len(df) < initial_len:
    print(f"🧹 {initial_len - len(df)} doublons supprimés.")

# Sélection des colonnes
df = df[['sepal_length', 'sepal_width', 'species']]

# Connexion et envoi dans la base de données
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')
df.to_sql('iris_data', engine, if_exists='replace', index=False)

print("✅ Données nettoyées et importées avec succès dans PostgreSQL.")