# файл для создания DAO и сервисов чтобы импортировать их везде
from dao.movie_dao import MovieDAO
from service.movie_service import MovieService
from setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(dao=movie_dao)