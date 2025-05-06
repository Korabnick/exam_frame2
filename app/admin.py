from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_basicauth import BasicAuth
from flask import url_for, redirect
from app.models import User, Role
from app.extensions import db

class AdminModelView(ModelView):
    def is_accessible(self):
        from flask_basicauth import BasicAuth
        auth = BasicAuth()
        return auth.authenticate()
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('admin.login'))

def setup_admin(app):
    admin = Admin(app, name='Admin Panel', template_mode='bootstrap3')
    
    # Добавляем модели в админ-панель
    admin.add_view(AdminModelView(User, db.session))
    admin.add_view(AdminModelView(Role, db.session))
    
    # Простая страница входа
    @app.route('/admin/login')
    def admin_login():
        return """
        <form action="/admin/" method="POST">
            <input type="hidden" name="url" value="/admin/">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
        """