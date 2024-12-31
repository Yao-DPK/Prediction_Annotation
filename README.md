# Backend documentation

## Prerequis

L'exécution de ce backend requiert en plus de `python3`, les librairies suivantes :

- **FastAPI**: framework Python moderne et rapide pour construire des API (Application Programming Interface) en utilisant le langage Python 3.7+. Il est conçu pour être facile à utiliser, rapide et robuste, avec une grande communauté de développeurs.

```bash
    pip install fastapi
```

- **Uvicorn**: bibliothèque Python qui fournit un serveur ASGI (Asynchronous Server Gateway Interface) léger et performant. Elle est conçue pour être utilisée avec les frameworks Python tels que FastAPI, qui nécessitent un serveur ASGI pour fonctionner.

```bash
    pip install "uvicorn[standard]"
```

- **Pydantic**: bibliothèque Python pour la validation de données et la définition de modèles de données. Elle permet de créer des modèles de données en utilisant les annotations de types Python 3.8+ et de valider automatiquement les données en les comparant aux modèles définis.

```bash
    pip install pydantic
```

## Exécuter le backend

Pour exécuter le backend, vous pouvez utiliser la commande suivante :

```bash
    uvicorn main:app --reload
```

Cela lancera le serveur ASGI et affichera un message de confirmation. Vous pouvez ensuite naviguer vers l'adresse http://localhost:8000 pour accéder au serveur API.

## Documentation de l'API

La documentation de l'API est disponible aux adresses suivantes :

- Swagger UI : http://localhost:8000/docs
- Redoc : http://localhost:8000/redoc

## Architecture du backend

Nous avons opté pour une architecture mololithique, avec un back-end en FastAPI, une base de données (PostgreSQL via SQLAlchemy) et le tout dans un même codebase. L’idée est de tout regrouper dans une seule application Python, structurée de façon modulaire, tout en restant un monolithe (un seul déploiement, un seul service).

```bash
tg-org-backend/
├── app/
│   ├── __init__.py
│   ├── main.py                # Point d'entrée de l'application FastAPI
│   ├── core/
│   │   ├── config.py          # Configuration générale (variables d'environnement, etc.)
│   │   ├── security.py        # Fonctions de hashing, génération de tokens, etc.
│   │   └── ...
│   ├── db/
│   │   ├── session.py         # Création de la session SQLAlchemy + moteur
│   │   └── base.py            # Base pour déclarer les modèles SQLAlchemy
│   ├── models/
│   │   ├── user.py            # Modèle utilisateur
│   │   ├── prediction.py      # Modèle pour les prédictions
│   │   ├── feedback.py        # Modèle pour les retours utilisateurs
│   │   ├── data.py            # (optionnel) Modèle pour les données brutes
│   │   └── __init__.py
│   ├── schemas/
│   │   ├── user.py            # Schémas Pydantic (UserIn, UserOut, etc.)
│   │   ├── prediction.py      # Schémas Pydantic pour les prédictions
│   │   ├── feedback.py
│   │   └── ...
│   ├── routers/
│   │   ├── auth.py            # Endpoints d’authentification
│   │   ├── predictions.py     # Endpoints pour gérer les prédictions
│   │   ├── feedbacks.py       # Endpoints pour gérer les retours/annotations
│   │   └── users.py           # Endpoints pour gérer les utilisateurs (créer, modifier, etc.)
│   ├── services/
│   │   ├── user_service.py    # Logique métier autour des utilisateurs
│   │   ├── prediction_service.py
│   │   └── feedback_service.py
│   └── utils/
│       ├── jwt.py             # Fonction de création/validation de token JWT
│       └── ...
├── tests/
│   ├── test_auth.py           # Tests unitaires pour l’auth
│   ├── test_predictions.py
│   └── ...
├── requirements.txt           # Dépendances (FastAPI, SQLAlchemy, psycopg2, etc.)
├── Dockerfile (optionnel)
├── docker-compose.yml (optionnel)
└── ...
```

- **`main.py`** : Point d’entrée unique où l’on crée l’application FastAPI et où l’on inclut les différents routers (auth, predictions, feedbacks...).
- **`routers/`** : Chaque fichier contient un “module” de routes (endpoints) correspondant à un domaine fonctionnel (authentification, gestion des prédictions, feedback, etc.), mais tout est réuni dans le même service FastAPI.
- **`services/`** : Contient la logique métier (ex. comment valider un feedback, comment enregistrer une prédiction, etc.).
- **`models/`** et **`schemas/`** : Séparent la définition de la structure en base (SQLAlchemy) et la validation (Pydantic).
- **`db/`** : Gère la session SQLAlchemy, la connexion à PostgreSQL, etc.
- **`core/`** : Fichiers de configuration et de sécurité (fonctions de hashage, paramétrage JWT, etc.).
- **`utils/`** : Fonctions utilitaires, par exemple pour gérer la génération et la vérification de tokens JWT.
