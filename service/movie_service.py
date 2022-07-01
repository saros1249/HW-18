from dao.movie_dao import MovieDAO


class MovieService:
    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movies(self, var) -> List["Movie"]:
        if var:
            movies = Movie.query.filter(Movie.var == var).all()
        else:
            movies = Movie.query.all()
        return self.movie_dao.get_movies(movies)





