from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy


from config import Configuartion  # import configuration data.

app = Flask(__name__)
# use values from our configuration object
app.config.from_object(Configuartion)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
