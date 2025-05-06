def test_get_users_unauthorized(client):
    """Test unauthorized access to users."""
    response = client.get('/api/users')
    assert response.status_code == 401

def test_get_users_authorized(client, user_headers):
    """Test authorized access to users."""
    response = client.get('/api/users', headers=user_headers)
    assert response.status_code == 200
    assert len(response.json) == 2  # admin and testuser

def test_create_user_admin(client, admin_headers):
    """Test user creation by admin."""
    response = client.post('/api/users', json={
        'username': 'newuser',
        'email': 'new@test.com',
        'password': 'Test1234'
    }, headers=admin_headers)
    assert response.status_code == 201
    assert response.json['username'] == 'newuser'