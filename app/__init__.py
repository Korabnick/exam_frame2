from flask import Flask
from .extensions import db, migrate, admin, basic_auth
from .logger import configure_logging
from .config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Инициализация расширений
    db.init_app(app)
    migrate.init_app(app, db)
    basic_auth.init_app(app)
    
    # Настройка Flask-Admin
    from app.views.admin_views import HomeAdminView, register_admin_views
    admin.init_app(app, index_view=HomeAdminView())
    register_admin_views()
    
    configure_logging(app)
    
    with app.app_context():
        db.create_all()
    
    return app