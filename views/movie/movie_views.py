# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

from flask_restx import Resource, Namespace



@movies_ns.route('/')
class MovieView(Resource):
    def get(self):
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







