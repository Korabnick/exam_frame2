import pytest
from app import create_app
from app.extensions import db as _db
from app.models import User, Role
from app.config import TestConfig
import os

@pytest.fixture(scope='session')
def app():
    """Create and configure a new app instance for tests."""
    app = create_app(TestConfig)
    
    with app.app_context():
        yield app

@pytest.fixture(scope='function')
def db(app):
    """Create a fresh test database for each test."""
    with app.app_context():
        _db.drop_all()
        _db.create_all()
        
        # Add test data
        admin_role = Role(name='admin', description='Administrator')
        user_role = Role(name='user', description='Regular User')
        _db.session.add_all([admin_role, user_role])
        _db.session.commit()
        
        admin = User(
            username='admin',
            email='admin@test.com',
            role_id=admin_role.id
        )
        admin.set_password('Sirius2025')
        
        regular_user = User(
            username='testuser',
            email='user@test.com',
            role_id=user_role.id
        )
        regular_user.set_password('testpassword')
        
        _db.session.add_all([admin, regular_user])
        _db.session.commit()
        
        yield _db
        
        _db.session.remove()
        _db.drop_all()

@pytest.fixture(scope='function')
def client(app, db):
    """Test client for the app."""
    with app.test_client() as client:
        with app.app_context():
            admin_role = Role.query.filter_by(name='admin').first()
            if not admin_role:
                admin_role = Role(name='admin', description='Administrator')
                db.session.add(admin_role)
                db.session.commit()

            admin = User.query.filter_by(username='admin').first()
            if not admin:
                admin = User(
                    username='admin',
                    email='admin@test.com',
                    role_id=admin_role.id
                )
                admin.set_password('Sirius2025')
                db.session.add(admin)
                db.session.commit()

            user_role = Role.query.filter_by(name='user').first()
            if not user_role:
                user_role = Role(name='user', description='Regular User')
                db.session.add(user_role)
                db.session.commit()

            regular_user = User.query.filter_by(username='testuser').first()
            if not regular_user:
                regular_user = User(
                    username='testuser',
                    email='user@test.com',
                    role_id=user_role.id
                )
                regular_user.set_password('testpassword')
                db.session.add(regular_user)
                db.session.commit()

        yield client

@pytest.fixture
def admin_headers(client):
    """Get admin auth headers."""
    response = client.post('/api/login', json={
        'username': 'admin',
        'password': 'Sirius2025'
    })
    return {'Authorization': f'Bearer {response.json["access_token"]}'}

@pytest.fixture
def user_headers(client):
    """Get regular user auth headers."""
    response = client.post('/api/login', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    return {'Authorization': f'Bearer {response.json["access_token"]}'}