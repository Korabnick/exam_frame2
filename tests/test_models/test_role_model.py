from app.models import Role

def test_role_creation(db):
    """Test role creation."""
    role = Role(name='moderator', description='Moderator')
    db.session.add(role)
    db.session.commit()
    
    assert role.id is not None
    assert role.name == 'moderator'
    assert Role.query.count() == 3  # admin, user, moderator

def test_role_relationships(db):
    """Test role-user relationships."""
    role = Role.query.filter_by(name='admin').first()
    assert len(role.users) == 1
    assert role.users[0].username == 'admin'

def test_role_repr(db):
    role = Role(name='test_role', description='Test Role')
    db.session.add(role)
    db.session.commit()
    assert repr(role) == "<Role test_role>"