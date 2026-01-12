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

```

---

## Installation

1 - Cloner le projet :

```bash
git clone https://github.com/kingcrud12/api-tests-python.git
cd api-tests-python
``` 

2 - Créer un environnement virtuel et installer les dépendances :

```bash
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows
pip install --upgrade pip
pip install -r requirements.txt
``` 

3- Lancer les tests 

Pour exécuter tous les tests avec affichage verbeux : 

```bash
pytest -v
``` 

4- Pour générer un rapport HTML :

```bash
pytest -v --html=reports/report.html --self-contained-html
``` 

5- Pipeline CI (GitHub Actions) 
Le projet inclut un workflow CI configuré dans `.github/workflows/api-tests.yml` qui :

* **S’exécute** à chaque `push` et `pull request`
* **Installe** Python `3.12` et les dépendances
* **Lance** tous les tests
* **Génère** un rapport HTML (à améliorer avec upload comme artefact si souhaité)

```bash
name: API Tests

on:
  push:
  pull_request:

jobs:
  api-tests:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: |
          pytest -v --html=reports/report.html --self-contained-html

``` 



