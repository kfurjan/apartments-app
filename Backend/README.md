# Backend (FastAPI & PostgreSQL)

Backend project (RESTful API) for apartmens-app. Project is being developed with Python (FastAPI framework) and PostgreSQL database.

## Project dependencies

- Python 3.8+
- Docker
- Visual Studio Code
- PyCharm IDE (Optional)

## First time setup

In order to enable IDE suggestions and autocompletion, dependencies should be installed locally before making any changes and starting to contribute to the project.

```bash
cd backend/
python3 -m venv env
source env/bin/activate
pip3 install -r app/requirements.txt
```

## Running unit tests

Unit tests are written using [pytest](https://docs.pytest.org/en/stable/) library for Python. Tests can be executed by following instructions below

```bash
cd tests/
pytest
```
