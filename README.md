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
git clone `lien-du-repo`
cd data-pipeline
```