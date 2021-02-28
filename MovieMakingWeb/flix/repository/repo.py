import abc
from typing import List

from flix.domainmodel.model import Director,Genre,Actor,Movie,Review,User, WatchList

repo_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_director(self, director: Director):
        raise NotImplementedError

    @abc.abstractmethod
    def get_director(self) -> Director:
        raise NotImplementedError

    @abc.abstractmethod
    def add_actor(self, actor: Actor):
        raise NotImplementedError

    @abc.abstractmethod
    def get_actor(self) -> Actor:
        raise NotImplementedError

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, movie: str):
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_movies(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_year(self, year) -> List[Movie]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_for_genre(self, genre_name: str):
        raise NotImplementedError

    @abc.abstractmethod
    def get_first_movie(self) -> Movie:
        raise NotImplementedError

    @abc.abstractmethod
    def get_last_movie(self) -> Movie:
        raise NotImplementedError

    @abc.abstractmethod
    def get_selected_movies(self, index_lst) -> List[Movie]:
        raise NotImplementedError

    @abc.abstractmethod
    def add_genre(self, genre: Genre):
        raise NotImplementedError

    @abc.abstractmethod
    def get_genre(self) -> List[Genre]:
        raise NotImplementedError

    @abc.abstractmethod
    def add_review(self, movie, comment, user):
        raise NotImplementedError

    @abc.abstractmethod
    def get_review(self):
        raise NotImplementedError

    @abc.abstractmethod
    def add_user(self, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def add_watchlst(self, movie):
        raise NotImplementedError

    @abc.abstractmethod
    def get_watchlst(self):
        raise NotImplementedError

    @abc.abstractmethod
    def remove_from_watchlist(self, username, movie):
        raise NotImplementedError