from datetime import date

from flix.domainmodel.model import Director, Genre, Actor, Movie, Review, User

import pytest


@pytest.fixture()
def movie():
    return Movie(
        "Moana", 2016
    )
@pytest.fixture()
def director():
    return Director("Taika Waititi")

def actor():
    return Actor("Angelina Jolie")

@pytest.fixture()
def user():
    return User('dbowie', '1234567890')


@pytest.fixture()
def genre():
    return Genre('Action')

def test_movie_construction(movie):
    assert movie.title == 'Moana'
    assert movie.year == 2016
    assert repr(
        movie) == '<Movie Moana, 2016>'
