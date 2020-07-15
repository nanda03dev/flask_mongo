import os
from flask import Flask

from .database import mongo_db
from os.path import join, dirname, realpath
UPLOAD_FOLDER = 'uploads'
UPLOAD_PATH = join(dirname(realpath(__file__)), UPLOAD_FOLDER)
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        UPLOAD_FOLDER = UPLOAD_PATH,
        ALLOWED_EXTENSIONS = ALLOWED_EXTENSIONS,
        MAX_CONTENT_LENGTH = MAX_CONTENT_LENGTH
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():
        # mongo db initiation
        mongo_db.start()
        
        from .routes import router
        # registering blueprints
        router.register(app)

        # a simple page that says hello

        @app.route('/notfound')
        def notfound():
            return 'notfound'

        return app
