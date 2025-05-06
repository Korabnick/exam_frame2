from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, create_access_token
from app.utils.decorators import admin_required

def test_admin_required_decorator():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test-secret'
    jwt = JWTManager(app)

    @app.route('/admin-test')
    @admin_required
    def admin_test():
        return jsonify({'message': 'success'})

    client = app.test_client()

    response = client.get('/admin-test')
    assert response.status_code == 401

    with app.app_context():
        token = create_access_token('user', additional_claims={'is_admin': False})
    
    response = client.get('/admin-test', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 403