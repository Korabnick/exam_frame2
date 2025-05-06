def test_api_spec(client):
    response = client.get('/api/spec')
    assert response.status_code == 200
    assert b'openapi' in response.data

def test_invalid_user_creation(client, admin_headers):
    response = client.post('/api/users', json={
        'username': 'a',  # too short
        'email': 'invalid',
        'password': 'short'
    }, headers=admin_headers)
    assert response.status_code == 400