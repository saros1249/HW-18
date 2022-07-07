# Класс работы с логикой.
from dao.genre_dao import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_genres(self, gid=None):
        """
        Получает из DAO данные о жанре и передаёт их в Views
        """
        return self.dao.get(gid)