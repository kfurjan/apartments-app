# Backend (FastAPI & PostgreSQL)

Backend project (RESTful API) for apartmens-app. Project is being developed with Python (FastAPI framework) and PostgreSQL database.
This repository will use [FastAPI real world example](https://github.com/nsidnev/fastapi-realworld-example-app) as a template.

## Project dependencies

- Python 3.8+
- Docker
- Visual Studio Code
- PyCharm IDE (Optional)

## Links to documentation

- REST API framework - [FastAPI](https://fastapi.tiangolo.com)
- JWT authorization library - [FastAPI JWT Auth](https://indominusbyte.github.io/fastapi-jwt-auth/)
- ORM tool - [SQLAlchemy](https://docs.sqlalchemy.org/en/14/)
- database migration tool - [alembic](https://alembic.sqlalchemy.org/en/latest/)
- unit test library - [pytest](https://docs.pytest.org/en/stable/)

## First time setup

In order to enable IDE suggestions and autocompletion, dependencies should be installed locally before making any changes and starting to contribute to the project.

```bash
cd backend/
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

## Running unit tests

Unit tests are written using [pytest](https://docs.pytest.org/en/stable/) library for Python. Tests can be executed by following instructions below

1. execute ```docker compose up --build```

2. using VS Code's Docker extension, attach shell to 'apartments-app_postgres_data' container

3. once in container shell, execute ```pytest -v tests/```
