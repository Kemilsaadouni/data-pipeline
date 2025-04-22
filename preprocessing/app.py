import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import time

# Wait for the database to be ready
time.sleep(10)

# Chargement du CSV
df = pd.read_csv('/data/iris.csv')

# Nettoyage rapide
df.columns = [col.strip().lower().replace('.', '_') for col in df.columns]

# Connexion à la base PostgreSQL
engine = create_engine('postgresql://user:password@db:5432/iris')

# Envoi dans PostgreSQL
df.to_sql('iris_data', engine, if_exists='replace', index=False)

print("✅ Données importées avec succès dans PostgreSQL")