#! /usr/bin/python

from flask.ext.script import Manager
from flask.ext.migrate import MigrateCommand

from application import app
from application import db
from tests import unittest

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def runserver():
    app.run(
        port=9999,
        debug=True)

@manager.command
def create_all_tables():
    db.create_all()

if __name__ == "__main__":
    manager.run()
