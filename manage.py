import codecs
import sadisplay
from datetime import datetime
import urllib.parse

from flask import jsonify, url_for
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import pytest

from app.bootstrap import create_app
from app.config import Config
from app.database import db
from app import models

app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('database', MigrateCommand)


@manager.command
def run():
    app.run(host=Config.APP_HOST, port=Config.APP_PORT)


@manager.command
def test():
    """Runs the tests."""
    pytest.main(["-s", "tests"])


@manager.command
def list_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.parse.unquote("{:50s} {:20s} {}".format(
            rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)


@manager.command
def seed():
    """Add seed data to the database."""
    print('Loading fixtures.')

    from seeds.seeder import Seeder
    Seeder(db=db).execute()

    db.session.commit()
    print('Done Seed.')


@manager.command
def generate_erd():
    desc = sadisplay.describe([getattr(models, attr) for attr in dir(models)])
    with codecs.open('documents/db/schema.plantuml', 'w', encoding='utf-8') as f:
        f.write(sadisplay.plantuml(desc))
    with codecs.open('documents/db/schema.dot', 'w', encoding='utf-8') as f:
        f.write(sadisplay.dot(desc))


if __name__ == '__main__':
    manager.run()
