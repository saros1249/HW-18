# Класс для работы с БД.
from dao.model.models import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get(self, mid=None, **kwargs):
        """
        Получение Фильма(-ов) из БД.
        :param mid: ID
        :param kwargs: Введённые парвметры для фильтрации (может быть жанр, год, режиссер)
        """
        query = self.session.query(Movie)

        if mid:
            return query.get(mid)

        if kwargs:
            for key, value in kwargs.items():
                query = query.filter(eval(f'Movie.{key}') == int(value))
        return query.all()

    def create(self, data):
        """
        Добавление записи к БД
        :param data: Данные для добавления.
        """
        new_movie = Movie(**data)
        with self.session.begin():
            self.session.add(new_movie)
        return new_movie

    def update(self, movie):
        """
        Редактирование записи.
        :param mid: ID
        :param data: Данные для замены.
        """
        self.session.add(movie)
        self.session.commit()

    def delete(self, mid):
        """
        Удаление записи.
        :param mid: ID
        """
        movie = self.get(mid)
        if not movie:
            return f'Фильм с ID{mid} не найден.', 404
        self.session.delete(movie)
        self.session.commit()
