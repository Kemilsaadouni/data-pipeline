# 📊 Iris Data Pipeline

## 📄 Description du projet

Ce projet est un pipeline complet de traitement et de modélisation de données autour du dataset **Iris**.  
L'objectif est de prédire la **longueur des sépales** (`sepal length`) à partir de leur **largeur** (`sepal width`), en utilisant un modèle **RandomForest** et un déploiement via une API dockerisée.

Nous utilisons **Docker**, **Docker Compose**, **PostgreSQL**, **MLflow**, **scikit-learn**, **FastAPI** et **SQLAlchemy** pour concevoir un projet modulaire, réplicable et traçable.

## ⚖️ Pré-requis

- Docker
- Docker Compose

Créer un fichier `.env` à la racine du projet avec les paramètres suivant en définissant les vôtres bien sûr:

```env
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=iris
POSTGRES_HOST=db
```

De plus, n'oubliez pas de démarrer les services **Docker** et notamment **Docker Desktop** avant de commencer l'installation.

## 🚀 Installation

Cloner le projet :
```bash
git clone <lien-du-repo>
cd data-pipeline
```

Construire les services :
```bash
docker-compose build --no-cache api
```

Démarrer le pipeline :
```bash
docker-compose up api
```

⚠️ Si il y a un problème n'hésitez pas à exécuter la commande suivante:
```bash
docker-compose down
```
➡️ ensuite recommencez à partir de l'étape de construction des services

## 📆 Démarrage et exploration

### API (FastAPI)
- Visitez : [http://localhost:8000](http://localhost:8000) — page d'accueil
- Documentation : [http://localhost:8000/docs](http://localhost:8000/docs) (Swagger UI)

Exemple de requête POST dans `/predict` :
```json
{
  "sepal_width": 3.1
}
```

Exemple de réponse attendue :
```json
{
  "predicted_sepal_length": 6.261679143079142
}
```

### MLflow UI

Accessible via : [http://localhost:5000](http://localhost:5000)

Permet de visualiser :
- Les expériences
- Les métriques (RMSE, etc...)
- Les versions de modèles

## 🎓 Accès à la base de données

Connexion la base de données depuis le conteneur Docker `db`:
```bash
docker exec -it db psql -U user -d iris
```

Commandes utiles :
```sql
-- Voir les tables
\dt

-- Aperçu des données
SELECT * FROM iris_data LIMIT 5;
```

## 🔎 Structure du projet

```bash
data-pipeline/
├── docker-compose.yml
├── .env
├── .gitignore
├── README.md
│
├── data/               # Dataset CSV
│   └── iris.csv
│
├── preprocessing/      # Preprocessing module
│   └── app.py
│   └── Dockerfile
│
├── model/              # Entraînement du modèle
│   └── train.py
│   └── Dockerfile
│
├── api/                # API FastAPI
│   └── main.py
│   └── Dockerfile
```
## 🤖 Fabriqué avec
- Python 3.10
- FastAPI
- scikit-learn
- PostgreSQL
- MLflow
- Docker / Docker Compose
- SQLAlchemy

## 🔄 Pistes d'amélioration
- Ajouter un Dockerfile personnalisé pour MLflow (stockage distant, tracking avancé)
- Étendre le modèle à d'autres features (ex. largeur/longueur des pétales)
- Meilleure gestion des erreurs dans l’API
- Créer une interface front (web) pour l'utilisateur final