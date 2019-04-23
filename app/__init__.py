from flask import Flask


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.settings')

    if config:
        app.config.update(config)

    @app.route('/')
    def home():
        return 'index'

    return app
