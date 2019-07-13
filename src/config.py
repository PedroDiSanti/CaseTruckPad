import os


class Development(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


app_config = {
    'development': Development
}
