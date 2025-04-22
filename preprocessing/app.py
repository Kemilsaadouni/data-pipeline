import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import time

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
engine = create_engine('postgresql://user:password@db:5432/iris')
df.to_sql('iris_data', engine, if_exists='replace', index=False)

print("✅ Données nettoyées et importées avec succès dans PostgreSQL.")