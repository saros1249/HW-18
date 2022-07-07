# Класс работы с логикой.
from dao.director_dao import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_directors(self, did=None):
        """
        Получает из DAO данные о режиссёре и передаёт их в Views
        """
        return self.dao.get(did)
