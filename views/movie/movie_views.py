# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service
from flask import request, make_response
from flask_restx import Resource, Namespace

from dao.model.schemas import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')

@movie_ns.route('/')
class MovieView(Resource):
    schema = MovieSchema(many=True)

    def get(self):
        movies = self.schema.dump(movie_service.get_movies(**request.args))
        return movies, 200


    def post(self):
        new_movie = movie_service.post_movie(request.json)
        resp = make_response('Новый фильм добавлен', 201)
        resp.headers['location'] = f'{movie_ns.path}/{new_movie.id}'
        return resp



@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    schema = MovieSchema()

    def get(self, mid: int):
        return self.schema.dump(movie_service.get_movies(mid)), 200

    def put(self, mid: int):
        movie = self.schema.dump(movie_service.update_movie_full(mid, request.json))
        return f'Запись с ID{mid} изменена на {movie}.', 200

    def patch(self, mid: int):
        movie = self.schema.dump(movie_service.update_movie_partially(mid, request.json))
        return f'Запись с ID{mid} изменена на {movie}.', 200

    def delete(self, mid: int):
        movie_service.delete(mid)
        return 204








