# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

from flask_restx import Resource, Namespace



@movies_ns.route('/')
class MovieView(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        return '', 200


    def post(self):
         return '', 201



@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get_one(self, mid):
        return '', 200

    def put(self, mid):
        return '', 201

    def patch(self, ,mid):
        return '', 201







