import pathlib

from flask import Flask, render_template
from werkzeug.exceptions import NotFound

auth_path = pathlib.Path(__file__).parent / "auth.py"
with open(auth_path, 'rt') as f:
    auth_code = f.read()


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev"
    )

    app.config.from_pyfile("config.py", silent=True)

    # apply the blueprints to the app
    from . import auth
    from . import programs

    app.register_blueprint(auth.bp)
    app.register_blueprint(programs.bp)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule("/", endpoint="index")

    @app.errorhandler(NotFound)
    def handle_404(e):
        return render_template("error.jinja", description=e.description, code=auth_code)

    return app
