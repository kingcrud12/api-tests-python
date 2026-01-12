# API Tests Automation – Python & Pytest

## Description

This project is an example of API test automation using Python and pytest, designed to demonstrate QA best practices and continuous integration.
It uses a public API (https://jsonplaceholder.typicode.com) to test CRUD endpoints (GET, POST, DELETE) and produce clear test reports

---

Technologies Used

Python 3.12

pytest for test execution

pytest-html for generating HTML reports

requests for HTTP requests

GitHub Actions for continuous integration (CI)

Git / GitHub for version control and CI pipeline

---

## Project structure

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

## Installation

1 - Clone project :

```bash
git clone https://github.com/kingcrud12/api-tests-python.git
cd api-tests-python
``` 

2- Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows
pip install --upgrade pip
pip install -r requirements.txt
``` 

3- Run the tests

```bash
pytest -v
``` 

4 - Generate an HTML report:

```bash
pytest -v --html=reports/report.html --self-contained-html
``` 

5- CI Pipeline (GitHub Actions)

The project includes a CI workflow configured in `.github/workflows/api-tests.yml` which:

* **Runs on every**  `push` et `pull request`
* **Installs** Python `3.12` and dependencies
* **Executes** all tests
* **Generates** an HTML report (can be improved with artifact upload if desired)

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



🌐 Read this project in: [French](README.md)
