import os

"""
Конфигурация Flask-приложения.
Содержит настройки секретного ключа, базы данных и папки загрузки обложек.
"""

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///exam.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static', 'covers')
