from urllib.parse import quote_plus


class Config:
    HOST_NAME = 'http://localhost'

    @staticmethod
    def init_app(app):
        pass


config = {
    'dev': Config,
}
