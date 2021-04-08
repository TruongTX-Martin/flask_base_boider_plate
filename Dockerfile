# ベースイメージ
FROM python:3.8

RUN pip install poetry

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /var/www
WORKDIR /var/www

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install --no-root

COPY . /var/www/app
WORKDIR /var/www/app

CMD ["poetry", "run", "python", "manage.py", "run"]
