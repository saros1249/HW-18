from dao.model.models import Movie


class MovieDAO:
    def get_movies(self):
        movies = Movie.query.all()
        return movies

    def get_movies_by_director(self, director):
        pass

    def get_movies_by_genre(self, genre):
        pass

    def get_movies_by_year(self,year):
        pass

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