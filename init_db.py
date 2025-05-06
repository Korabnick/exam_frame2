from app import create_app
from app.models import db, Role, User
from app.config import Config

app = create_app()

with app.app_context():
    db.create_all()
    
    roles = [
        ('admin', 'Administrator with full access'),
        ('user', 'Regular user with read-only access')
    ]
    
    for name, description in roles:
        if not Role.query.filter_by(name=name).first():
            db.session.add(Role(name=name, description=description))
    
    db.session.commit()
    
    admin_role = Role.query.filter_by(name='admin').first()
    if not User.query.filter_by(username=Config.FLASK_ADMIN_USER).first():
        admin = User(
            username=Config.FLASK_ADMIN_USER,
            email='admin@example.com',
            role_id=admin_role.id
        )
        admin.set_password(Config.FLASK_ADMIN_PASSWORD)
        db.session.add(admin)
        db.session.commit()