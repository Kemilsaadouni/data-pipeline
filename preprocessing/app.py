# import pandas as pd
# import psycopg2
# from sqlalchemy import create_engine
# import time
# 
# # Wait for the database to be ready
# time.sleep(10)
# 
# # Chargement du CSV
# df = pd.read_csv('/data/iris.csv')
# 
# # Nettoyage rapide
# df.columns = [col.strip().lower().replace('.', '_') for col in df.columns]
# 
# # Connexion à la base PostgreSQL
# engine = create_engine('postgresql://user:password@db:5432/iris')
# 
# # Envoi dans PostgreSQL
# df.to_sql('iris_data', engine, if_exists='replace', index=False)
# 
# print("✅ Données importées avec succès dans PostgreSQL")

import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import time

# Attente pour que la base soit prête
time.sleep(10)

# 1. Chargement du fichier CSV
df = pd.read_csv('/data/iris.csv')

# 2. Nettoyage des noms de colonnes (standardisation)
df.columns = [col.strip().lower().replace('.', '_') for col in df.columns]

# 3. Vérification et suppression des valeurs manquantes
if df.isnull().sum().sum() > 0:
    print("⚠️ Données manquantes détectées, suppression en cours...")
    df.dropna(inplace=True)

# 4. Suppression des doublons
initial_len = len(df)
df.drop_duplicates(inplace=True)
if len(df) < initial_len:
    print(f"🧹 {initial_len - len(df)} doublons supprimés.")

# 5. Suppression des colonnes inutiles pour ce projet
df = df[['sepal_length', 'sepal_width']]

# 6. Connexion à PostgreSQL via SQLAlchemy
engine = create_engine('postgresql://user:password@db:5432/iris')

# 7. Envoi dans la base
df.to_sql('iris_data', engine, if_exists='replace', index=False)

print("✅ Données nettoyées et importées avec succès dans PostgreSQL.")