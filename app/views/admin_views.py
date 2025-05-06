from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from app.extensions import admin, basic_auth, db
from app.models import User, Role

class HomeAdminView(AdminIndexView):
    def is_accessible(self):
        return basic_auth.authenticate()
    
    def inaccessible_callback(self, name, **kwargs):
        return basic_auth.challenge()

class AdminModelView(ModelView):
    def is_accessible(self):
        return basic_auth.authenticate()
    
    def inaccessible_callback(self, name, **kwargs):
        return basic_auth.challenge()

# Регистрация представлений
def register_admin_views():
    admin.add_view(AdminModelView(User, db.session, name='Users'))
    admin.add_view(AdminModelView(Role, db.session, name='Roles'))