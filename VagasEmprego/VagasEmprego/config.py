
class Config:
    SECRET_KEY = 'hard to guess string'
    UPLOAD_FOLDER = 'static/images'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///pets.db'

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_pets.db'
