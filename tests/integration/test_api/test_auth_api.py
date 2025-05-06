def test_login_success(client):
    """Test successful login."""
    response = client.post('/api/login', json={
        'username': 'admin',
        'password': 'Sirius2025'
    })
    assert response.status_code == 200
    assert 'access_token' in response.json

def test_login_failure(client):
    """Test failed login."""
    response = client.post('/api/login', json={
        'username': 'admin',
        'password': 'wrongpass'
    })
    assert response.status_code == 401