from app.extensions import db
from .user import User
from .role import Role

__all__ = ['User', 'Role', 'db']