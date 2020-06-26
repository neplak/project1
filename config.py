import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = b'\xf9\x05p\xff\xc8X\x86\xa7 c\xf3X\xfb-\x11\xa4q\x96\x12xK\xde4Db\xd8\x83D\x8f\xb4sihf\x12\xee\xeb\xe4\xb3\xa8*A\x7fW9\xe1\xf5|\xac\x97\xd4\xd13\xf03\xa9e\xd6\xbc\xec_b\x8e\x10'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://books:bNcO9ypR@192.168.1.120:5432/books'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SESSION_PERMANENT=False
    SESSION_TYPE="filesystem"
    TEMPLATE_FOLDER='my_templates'
    STATIC_FOLDER="my_scripts"

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
