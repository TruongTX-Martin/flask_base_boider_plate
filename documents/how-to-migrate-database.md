# How to migrate database

In this code base, we are using Flask-SQLAlchemy for handling the database access, and Flask-Migrate for managing multiple revisions of database.

- Flask-SQLAlchemy - Flask extension that provides SQLAlchemy support
- Flask-Migrate - extension that supports SQLAlchemy database migrations via Alembic

## Prepare database on local

```bash
$ mysql -uroot
mysql> CREATE DATABA flask_app_base_local;
mysql> CREATE USER 'dbuser'@'%' IDENTIFIED BY 'password';
mysql> GRANT ALL ON flask_app_base_local.* TO 'dbuser'@'%';
```

Update your .env file for database

```bash
cp .env.example .env

```

Flask-Migrate makes use of Flasks new CLI tool. However, this article uses the interface provided by Flask-Script, which was used before by Flask-Migrate. In order to use it, you need to install it via:
You can check `manage.py` file.

```python
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('database', MigrateCommand)

```

## Initialize database migration

```
poetry run python manage.py database init

```
After you run the database initialization you will see a new folder called “migrations” in the project. This holds the setup necessary for Alembic to run migrations against the project. Inside of “migrations” you will see that it has a folder called “versions”, which will contain the migration scripts as they are created.


## Migrate database

To sets the revision in the database to head
```bash
poetry run python manage.py database stamp head

```

## Create or update a model

Set up a basic model by adding a models.py file:

```python
import datetime

from ..database import db


class File(db.Model):
    __tablename__ = 'files'

    id = db.Column('id', db.BigInteger, primary_key=True)
    original_file_name = db.Column('original_file_name',
                                   db.String(255),
                                   nullable=True)
    url = db.Column('url', db.String(255), nullable=False)
    media_type = db.Column('media_type', db.String(255), nullable=True)
    storage_type = db.Column('storage_type', db.String(255), nullable=True)
    created_at = db.Column('created_at',
                           db.TIMESTAMP,
                           default=datetime.datetime.utcnow,
                           nullable=False)
    updated_at = db.Column('updated_at',
                           db.TIMESTAMP,
                           onupdate=datetime.datetime.utcnow,
                           default=datetime.datetime.utcnow,
                           nullable=False)

    def __repr__(self):
        return "<{name} '{id}'>".format(name=self.__class__.__name__,
                                        id=self.id)
```

Here we created a table to store the files.
JSON columns are fairly new to Postgres and are not available in every database supported by SQLAlchemy so we need to import it specifically.
Next we created a File() class and assigned it a table name of results. 

We then created an __init__() method that will run the first time we create a new result and, finally, a __repr__() method to represent the object when we query for it.

## Migrate database

Let’s create our first migration by running the migrate command.

Generate the migration file.

```bash
poetry run python manage.py database migrate -m 'create users table'
```

Update database

```bash
poetry run python manage.py database upgrade

```

## Update the ERD for document


```bash
poetry run python manage.py generate_erd
```

## Common issues

- [Resolving Database Schema Conflicts](https://blog.miguelgrinberg.com/post/resolving-database-schema-conflicts)
- [Work on multiple Git branches](https://stackoverflow.com/questions/55715129/work-on-multiple-branches-with-flask-migrate)

