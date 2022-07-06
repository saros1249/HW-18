from dao.model.models import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get(self, mid=None, **kwargs):
        query = self.session.query(Movie)

        if kwargs:
            for key, value in kwargs.items():
                query = query.filter(eval(f'Movie.{key}') == int(value))

        if mid:
            movies = query.get(mid)
        else:
            movies = query.all()
        return movies

    def get_one_movie(self, mid):
        pass

    def post_movie(self):
        pass

    def put_movie(self, mid):
        pass

    def patch_movie(self, mid):
        pass

    def delete_movie(self, mid):
        pass