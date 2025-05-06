from app.models import User, Role
from app.extensions import db
from app.config import Config

def create_admin_user():
    admin_role = Role.query.filter_by(name='admin').first()
    if not admin_role:
        admin_role = Role(name='admin', description='Administrator')
        db.session.add(admin_role)
        db.session.commit()

    admin_user = User.query.filter_by(username=Config.FLASK_ADMIN_USER).first()
    if not admin_user:
        admin_user = User(
            username=Config.FLASK_ADMIN_USER,
            email='admin@example.com',
            role_id=admin_role.id
        )
        admin_user.set_password(Config.FLASK_ADMIN_PASSWORD)
        db.session.add(admin_user)
        db.session.commit()

def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user
    return None