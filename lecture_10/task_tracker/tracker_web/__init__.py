import click
from flask import Flask
from flask_bootstrap import Bootstrap

bs = Bootstrap()


def create_app():
    app = Flask(__name__,
                static_folder='static',
                template_folder='templates'
                )
    bs.init_app(app)
    from .views import bp
    app.register_blueprint(bp)
    return app
