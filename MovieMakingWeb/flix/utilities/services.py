from typing import Iterable
import random

from flix.repository.repo import AbstractRepository
from flix.domainmodel.model import Movie


def get_genre_names(repo: AbstractRepository):
    genres = repo.get_genre()
    gen_names = [gen for gen in genres]

    return genres


def get_random_movies(quantity, repo: AbstractRepository):
    movies_total = repo.get_number_of_movies()
    print(movies_total)
    if quantity >= movies_total:
        # Reduce the quantity of ids to generate if the repository has an insufficient number of articles.
        quantity = movies_total - 1

    # Pick distinct and random articles.
    random_m = random.sample(range(1, movies_total), quantity)
    movies = repo.get_selected_movies(random_m)

    return movies#movies_to_dict(movies)


# ============================================
# Functions to convert dicts to model entities
# ============================================

def movie_to_dict(movie: Movie):
    movie_dict = {
        'title': movie.title,
    }

    return movie_dict


def movies_to_dict(movies: Iterable[Movie]):
    return [movie_to_dict(movie) for movie in movies]