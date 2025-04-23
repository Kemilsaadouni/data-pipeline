# 📊 Iris Data Pipeline

## 📄 Description du projet

Ce projet est un pipeline complet de traitement et de modélisation de données autour du dataset **Iris**.  
L'objectif est de prédire la **longueur des sépales** (`sepal length`) à partir de leur **largeur** (`sepal width`), en utilisant un modèle **RandomForest** et un déploiement via une API dockerisée.

Nous utilisons **Docker**, **Docker Compose**, **PostgreSQL**, **MLflow**, **scikit-learn**, **FastAPI** et **SQLAlchemy** pour concevoir un projet modulaire, réplicable et traçable.

---

## ✨ Pour commencer

Voici comment démarrer rapidement le projet sur votre machine.

---

## ⚖️ Pré-requis

- Docker  
- Docker Compose  

Créer un fichier `.env` à la racine du projet avec le contenu suivant :

```env
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=iris
POSTGRES_HOST=db
