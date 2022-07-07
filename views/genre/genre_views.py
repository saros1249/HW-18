from flask_restx import Resource, Namespace

from dao.model.schemas import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenreView(Resource):
    schema = GenreSchema(many=True)

    def get(self):
        return self.schema.dump(genre_service.get_genres()), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    schema = GenreSchema()

    def get(self, gid):
        return self.schema.dump(genre_service.get_genres(gid)), 200
