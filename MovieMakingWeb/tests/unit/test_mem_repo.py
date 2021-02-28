from datetime import date, datetime
from typing import List

import pytest

from flix.domainmodel.model import Director, Genre, Actor, Movie, Review, User
from flix.repository.repo import RepositoryException


def test_repository_can_add_a_user(in_memory_repo):
    user = User('Dave', '123456789')
    in_memory_repo.add_user(user)

    assert in_memory_repo.get_user('dave') is user


def test_repository_can_retrieve_a_user(in_memory_repo):
    user = User('fmercury', '123456789')
    in_memory_repo.add_user(user)
    user = in_memory_repo.get_user('fmercury')
    assert user == User('fmercury', '8734gfe2058v')


def test_repository_does_not_retrieve_a_non_existent_user(in_memory_repo):
    user = in_memory_repo.get_user('prince')
    assert user is None

def test_repository_can_add_movie(in_memory_repo):
    movie = Movie(
        'Moana', 2016
    )
    in_memory_repo.add_movie(movie)

    assert in_memory_repo.get_movie('Moana') is movie


def test_repository_can_retrieve_movie(in_memory_repo):
    movie = in_memory_repo.get_movie('Moana')

    # Check that the Article has the expected title.
    assert movie.title == 'Moana'


def test_repository_does_not_retrieve_a_non_existent_movie(in_memory_repo):
    movie = in_memory_repo.get_movie('abbveav')
    assert movie is None


def test_repository_can_add_a_genre(in_memory_repo):
    gen = Genre('Thriller')
    in_memory_repo.add_genre(gen)

    assert gen in in_memory_repo.get_genre_lst()


def test_repository_can_add_a_comment(in_memory_repo):
    in_memory_repo.add_review('Moana', "Good movie!", 'thorke')

    assert in_memory_repo.get_review('Moana') != []


def test_repository_does_not_add_a_comment_without_a_user(in_memory_repo):
    with pytest.raises(RepositoryException):
        in_memory_repo.add_review("Moana", "Good Movie!", None)


def test_repository_can_retrieve_comments(in_memory_repo):
    in_memory_repo.add_review('Moana', "Good movie!", 'thorke')
    assert len(in_memory_repo.get_review("Moana")) == 1