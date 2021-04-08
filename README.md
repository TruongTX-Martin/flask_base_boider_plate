# How to setup project

This project uses `pyproject.toml` proposed on [PEP-0518](https://www.python.org/dev/peps/pep-0518/#specification) instead of `requirements.txt`. And you can use [Poetry](https://python-poetry.org/).

## 1. Setup python 3.8.x environment with `pyenv` and install Poetry

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
poetry install
```

- Run http server

```
poetry run python manage.py run
```


## How to run with Docker compose

We have 2 container for local development. Please check detail configuration in `docker-compose.yml`

- db: Postgres database with initiate database process in `docker/init.sql`
- app: oppi application

```
cd oppi_mvp
docker-compose up
```

#### How to execute a poetry command in side docker-compose container
For example with `poetry run python manage.py database upgrade` command you can run through `docker-compose exec`

```bash
docker-compose exec app poetry run python manage.py database upgrade

```

## How to update database

### 1. Update models files
Please update your model files by adding new fields or add new model

### 2. Update database

```bash
poetry run python manage.py database upgrade
```

### 3. Generate migration files
```bash
poetry run python manage.py database migrate
```

### Code format

Please execute isort and yapf before committing

```bash

poetry run isort -rc -y .

poetry run yapf -ir -vv .
```
