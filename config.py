import os

class Config:
    """
    General configuration class
    """
    SECRET_KEY = 'SECRET_KEY'
    
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    # Email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'simon.mureithi@student.moringaschool.com'
    MAIL_PASSWORD = 'prince070202'


class ProdConfig(Config):
    """
    Production configuration class
    """
    # SQLALCHEMY_DATABASE_URI = 'postgresql://pykonncljnjurg:ca9419f42cf10926d49c52fd2a8e7b5e3c63b3d4d9b419d32a77c3b4d04c801c@ec2-18-214-140-149.compute-1.amazonaws.com:5432/dekiu1uqvid4ta?sslmode=require'


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/pitches_test'



class DevConfig(Config):
    """
    Development configuration class
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/pitches'
    DEBUG = True
    



config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
