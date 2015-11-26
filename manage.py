

from flask.ext.script import Manager, Server
from flask.ext.migrate import MigrateCommand

from flaskdash.app import create_app

app = create_app()
manager = Manager(app)

manager.add_command("runserver", Server("localhost", port=8080))
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
