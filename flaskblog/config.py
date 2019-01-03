import json

with open('flaskblog/config.json') as config_file:
        config = json.load(config_file)

class Config:
    SECRET_KEY = config.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = config.get('MAIL_SERVER')
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = config.get('EMAIL_USER')
    MAIL_PASSWORD = config.get('EMAIL_PASS')
    GOOGLE_CLIENT_ID = config.get('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = config.get('GOOGLE_CLIENT_ID')
