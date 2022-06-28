# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

from flask_restx import Resource, Namespace



@genres_ns.route('/')
class GenreView(Resource):
    def get(self):
         return '', 200


    def post(self):
         return '', 201



@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get_one(self, gid):
        return '', 200

    def put(self, gid):
        return '', 201

    def patch(self, gid):
        return '', 201







