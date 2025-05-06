from app.models import User

def test_user_creation(db):
    """Test user creation."""
    existing_user = User.query.filter_by(username='newuser').first()
    if existing_user:
        db.session.delete(existing_user)
        db.session.commit()

    user = User(
        username='newuser',
        email='new@test.com',
        role_id=2  # user role
    )
    user.set_password('password123')
    db.session.add(user)
    db.session.commit()
    
    assert user.id is not None
    assert user.check_password('password123')
    assert not user.check_password('wrongpass')
    
    db.session.delete(user)
    db.session.commit()

def test_user_admin_check(db):
    """Test is_admin check."""
    db.session.rollback()
    
    admin = User.query.filter_by(username='admin').first()
    user = User.query.filter_by(username='testuser').first()
    
    assert admin.is_admin
    assert not user.is_admin

def test_user_repr(db):
    user = User(
        username='repruser',
        email='repr@test.com',
        role_id=2
    )
    db.session.add(user)
    db.session.commit()
    assert repr(user) == "<User repruser>"