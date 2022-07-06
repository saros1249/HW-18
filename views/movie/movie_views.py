# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service
from flask import request
from flask_restx import Resource, Namespace

from dao.model.schemas import MovieSchema
from service.movie_service import MovieService

movie_ns = Namespace('movies')

@movie_ns.route('/')
class MovieView(Resource):
    def get(self):
        schema = MovieSchema(many=True)
        movies = schema.dump(MovieService.get_movies(**request.args))
        return movies, 200


    def post(self):
         return '', 201



@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get_one(self, mid):
        return '', 200

    def put(self, mid):
        return '', 201

    def patch(self, mid):
        return '', 201







