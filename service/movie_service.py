# Класс для работы с логикой.
from dao.movie_dao import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_movies(self, mid=None, **kwargs):
        """
        Получение Фильма(-ов).
        :param mid: ID
        :param kwargs: Введённые парвметры для фильтрации (может быть жанр, год, режиссер)
        """
        return self.dao.get(mid, **kwargs)

    def post_movie(self, data):
        """
        Добавление записи.
        :param data: Данные для добавления.
        """
        return self.dao.create(data)

    def update_movie_full(self, mid, data):
        """
        Полная замена записи.
        :param mid: ID
        :param data: Данные для замены.
        """
        movie = self.get_movies(mid)

        movie.title = data['title']
        movie.description = data['description']
        movie.trailer = data['trailer']
        movie.year = data['year']
        movie.rating = data['rating']
        movie.genre_id = data['genre_id']
        movie.director_id = data['director_id']
        self.dao.update(movie)
        return movie

    def update_movie_partially(self, mid, data):
        """
        Частичное редактирование записи.
        :param mid: ID
        :param data: Данные для редактирования в виде словарья.
        :return:
        """
        movie = self.get_movies(mid)

        if 'title' in data:
            movie.title = data['title']
        if 'description' in data:
            movie.description = data['description']
        if 'trailer' in data:
            movie.trailer = data['trailer']
        if 'year' in data:
            movie.year = data['year']
        if 'rating' in data:
            movie.rating = data['rating']
        if 'genre_id' in data:
            movie.genre_id = data['genre_id']
        if 'director_id' in data:
            movie.director_id = data['director_id']
        self.dao.update(movie)
        return movie

    def delete(self, mid):
        """
        Удаление записи.
        :param mid: ID
        """
        self.dao.delete(mid)
