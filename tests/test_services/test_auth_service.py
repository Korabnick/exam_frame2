from app.services.auth import authenticate_user

def test_authenticate_user_success(db):
    """Test successful authentication."""
    db.session.rollback()
    
    user = authenticate_user('admin', 'Sirius2025')
    assert user is not None
    assert user.username == 'admin'

def test_authenticate_user_failure(db):
    """Test failed authentication."""
    db.session.rollback()
    
    assert authenticate_user('admin', 'wrongpass') is None
    assert authenticate_user('nonexistent', 'pass') is None