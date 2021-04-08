# How run in local environment


## Using pyenv, poetry

This project uses `pyproject.toml` proposed on [PEP-0518](https://www.python.org/dev/peps/pep-0518/#specification) instead of `requirements.txt`. And you can use [Poetry](https://python-poetry.org/).

### 1. Setup python 3.8.x environment with `pyenv` and install Poetry

- Install [pyenv](https://github.com/pyenv/pyenv)
- Install latest version of python 3.8.x and use it.

```
pyenv install 3.8.0
pyenv local 3.8.0
```

- Install [Poetry](https://python-poetry.org/)

```
pip3 install poetry
```

- Install dependency

```
cd flask-app-base
poetry install
```

- Update environment variables

```
cp .env.example .env
```
Please update the database information with DB_ environment variables in .env file

- Run http server

```
poetry run python manage.py run
```

## How to update database

### 1. Update models files
Please update your model files by adding new fields or add new model

Please read detail in [how-to-migrate-database.md](./how-to-migrate-database.md)


### 2. Update database

```bash
poetry run python manage.py database upgrade
```

## 3. Generate migration files
```bash
poetry run python manage.py database migrate
```

## Python code format

Please execute isort and yapf before committing

```bash

poetry run isort -rc -y .

poetry run yapf -ir -vv .
```

## Run unittest

For unittest implement please see [unittest.md](./unittest.md) 
```
poetry run python manage.py test
```

## Generate ERD

We are using PlantUML to manage ERD. Please install plantUML extension to your IDE to view the file.

ERD: [/documents/db/schema.plantuml](./db/schema.plantuml)

Auto generate ERD
```
poetry run manage.py generate_erd
```

## How to run with Docker compose

We have 2 container for local development. Please check detail configuration in `docker-compose.yml`

- db: Mysql database with initiate database process in `docker/init.sql`
- app: flask-app-base application

Update environment variables

```
cp .env.example .env
```

Please update the database information with DB_ environment variables in .env file. For DB host please using docker-compose service name instead of `localhost` as default.

```
cd flask-app-base
docker-compose up
```

#### How to execute a poetry command in side docker-compose container

For example with `poetry run python manage.py database upgrade` command you can run via `docker-compose exec`

```bash
docker-compose exec app poetry run python manage.py database upgrade

```
