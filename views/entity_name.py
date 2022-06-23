# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

from flask_restx import Resource, Namespace

film_ns = Namespace('film')
director_ns = Namespace('director')
genre_ns = Namespace('genre')


@book_ns.route('/')
class BooksView(Resource):
    def get(self):
         return '', 200

    def get_one(self, fid):
        return '', 200

    def post(self):
         return '', 201

    def patch(self, fid):
        return '', 201



