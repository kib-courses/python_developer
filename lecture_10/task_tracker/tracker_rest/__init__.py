import click
from flask import Flask
from flask.cli import with_appcontext


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('resource/api.cfg')

    # bind db helper and marshmallow
    from .api_v1.models import db
    db.init_app(app)
    from .api_v1.schemas import ma
    ma.init_app(app)

    # init blueprints
    from task_tracker.tracker_rest import api_v1
    app.register_blueprint(api_v1.bp)

    # register cli funcs
    app.cli.add_command(init_db_command)

    return app


def init_db():
    from .api_v1.models import db
    db.drop_all()
    db.create_all()


@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Initialized the database.")


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
