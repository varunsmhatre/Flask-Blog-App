import os

root_path = os.path.split(os.path.realpath(__file__))[0]

class  Config:
    # root_path = r'c:\enter your absolute path\Flask_Blog\flaskblog'
    SECRET_KEY = '7e6605f314f6925dc7b04ed809770bae'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{root_path}/site.db'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'your mail id'
    MAIL_PASSWORD = 'your mail password'
