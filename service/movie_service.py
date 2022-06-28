from dao.movie_dao import MovieDAO


class MovieService:
    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movies(self):# -> List["Movie"]:

        return self.movie_dao.get_movies()





