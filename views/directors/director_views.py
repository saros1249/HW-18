

from flask_restx import Resource, Namespace



@directors_ns.route('/')
class DirectorView(Resource):
    def get(self):
         return '', 200


    def post(self):
         return '', 201



@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get_one(self, mid):
        return '', 200

    def put(self, did):
        return '', 201

    def patch(self, did):
        return '', 201







