from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.movie.movie_views import movie_ns


def create_app(config):
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    return application


def register_extensions(application: Flask):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    create_data(application, db)




def create_data(application, dbase):
    with application.app_context():
        dbase.create_all()



if __name__ == '__main__':
    app = create_app(Config())
    register_extensions(app)
    app.run()
