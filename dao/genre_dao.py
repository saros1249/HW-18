# Класс для работы с БД.
from dao.model.models import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get(self, gid=None):
        """
        Получение Жанра(-ов)
        :param gid: ID
        """
        query = self.session.query(Genre)

        if gid:
            return query.get(gid)
        return query.all()
