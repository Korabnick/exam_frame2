from flask import Blueprint, render_template, request, redirect, url_for
from flask_basicauth import BasicAuth
from werkzeug.security import check_password_hash
from app.extensions import basic_auth
from app.config import Config

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if (username == Config.BASIC_AUTH_USERNAME and 
            password == Config.BASIC_AUTH_PASSWORD):
            return redirect(url_for('admin.index'))
    
    return render_template('auth/login.html')