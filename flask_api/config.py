import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    HOST_NAME = 'http://localhost'

    @staticmethod
    def init_app(app):
        pass


config = {
    'dev': Config,
}
