from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.directors.director_views import director_ns
from views.genre.genre_views import genre_ns
from views.movie.movie_views import movie_ns


def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    register_extensions(application)
    application.app_context().push()
    return application


def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


app = create_app(Config())

if __name__ == '__main__':
    app.run()
