# API Tests Automation – Python & Pytest

## Description

Ce projet est un exemple de **tests automatisés d’API** utilisant **Python** et **pytest**, conçu pour démontrer les bonnes pratiques QA et l’intégration continue.  
Il utilise une API publique (`https://jsonplaceholder.typicode.com`) pour tester des endpoints CRUD (GET, POST, DELETE) et produire des rapports de tests clairs.

---

## Technologies utilisées

- **Python 3.12**
- **pytest** pour l’exécution des tests
- **pytest-html** pour la génération de rapports HTML
- **requests** pour les appels HTTP
- **GitHub Actions** pour l’intégration continue (CI)
- **Git / GitHub** pour la gestion de versions et le pipeline CI

---

## Structure du projet

```text
api-tests-python/
├── requirements.txt          # Dépendances Python
├── tests/                    # Dossier contenant tous les tests
│   ├── conftest.py           # Fixtures pytest globales
│   ├── test_users.py         # Tests CRUD pour les utilisateurs
│   ├── test_posts.py         # Tests CRUD pour les posts
│   ├── test_delete_post.py   # Tests suppression de posts
│   ├── test_get_user_by_id.py
│   ├── test_get_user_not_found.py
│   └── reports/              # Rapports HTML générés par pytest-html
└── README.md
