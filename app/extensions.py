from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_basicauth import BasicAuth

db = SQLAlchemy()
migrate = Migrate()
basic_auth = BasicAuth()

admin = Admin(name='Admin Panel', template_mode='bootstrap3')