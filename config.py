import os

import app


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/morocco_tour_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app.config.from_object(Config)
