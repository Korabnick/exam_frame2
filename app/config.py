import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    SECRET_KEY = os.getenv('SECRET_KEY', 'super-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI', 'postgresql://user:password@db:5432/app_db') + '?client_encoding=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN_USER = os.getenv('FLASK_ADMIN_USER', 'admin')
    FLASK_ADMIN_PASSWORD = os.getenv('FLASK_ADMIN_PASSWORD', 'Sirius2025')
    BASIC_AUTH_USERNAME = os.getenv('FLASK_ADMIN_USER', 'admin')
    BASIC_AUTH_PASSWORD = os.getenv('FLASK_ADMIN_PASSWORD', 'Sirius2025')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://exam:exam_password@localhost:5432/exam_db_test'
    JWT_SECRET_KEY = 'test-secret-key'
    REDIS_URL = 'redis://localhost:6379/1'