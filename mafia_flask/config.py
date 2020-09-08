import os


class Config:
    SECRET_KEY = 'b3a7f6f1bf1ecb4d3197d57c361251e4'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('my_email')
    MAIL_PASSWORD = os.environ.get('my_password')
