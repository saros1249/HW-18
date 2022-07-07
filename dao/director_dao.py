# Класс для работы с БД
from dao.model.models import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get(self, did=None):
        """
        Получение Режисёра(-ов) из БД
        :param did: ID
        """
        query = self.session.query(Director)

        if did:
            return query.get(did)
        return query.all()