import sys
from flask import Flask
from werkzeug.serving import run_simple


def create_app():
    app = Flask(__name__)
    from .views import bp

    app.register_blueprint(bp)
    return app


if __name__ == '__main__':
    run_simple('0.0.0.0', 5000, create_app())
