# config.py
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'secretkey')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///formdata.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
