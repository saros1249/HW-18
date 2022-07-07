from dao.movie_dao import MovieDAO
from service.movie_service import MovieService
from dao.director_dao import DirectorDAO
from service.director_service import DirectorService
from dao.genre_dao import GenreDAO
from service.genre_service import GenreService
from setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(dao=movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(dao=director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(dao=genre_dao)
