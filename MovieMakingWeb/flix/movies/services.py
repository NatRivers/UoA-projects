from typing import List, Iterable

from flix.repository.repo import AbstractRepository
from flix.domainmodel.model import make_review, Movie, Review, Genre, WatchList


class NonExistentMovieException(Exception):
    pass


class UnknownUserException(Exception):
    pass


def add_review(movie: str, review_text: str, username: str, repo: AbstractRepository):
    # Check that the article exists.
    mov = repo.get_movie(movie)
    if mov is None:
        raise NonExistentMovieException

    user = repo.get_user(username)
    if user is None:
        raise UnknownUserException

    # Create comment.
    #review = make_review(review_text, user, movie, )

    # Update the repository.
    repo.add_review(movie, review_text, username)

def get_movie(movie: str, repo: AbstractRepository):
    movie = repo.get_movie(movie)

    if movie is None:
        raise NonExistentMovieException

    return movie_to_dict(movie)


def get_movies_for_genre(genre_name, repo: AbstractRepository):
    movies = repo.get_movie_for_genre(genre_name)
    return movies


def get_reviews_for_movie(mov: str, repo: AbstractRepository):
    rev_dict = repo.get_review_lst()
    if mov in rev_dict:
        reviews = repo.get_review(mov)
    else:
        return []
    return reviews

def add_to_watchlist(username, movie, repo: AbstractRepository):
    repo.add_watchlst(username, movie)

def get_watchlist(username, repo: AbstractRepository):
    lst = repo.get_watchlst(username)
    return lst

def remove_watchlst_movie(username, movie, repo: AbstractRepository):
    repo.remove_from_watchlist(username, movie)
    movies_in_lst = repo.get_watchlst(username)
    return movies_in_lst


# ============================================
# Functions to convert model entities to dicts
# ============================================

def movie_to_dict(movie: Movie):
    movie_dict = {
        'title': movie.title,
        'year': movie.year,
    }
    return movie_dict


#def movies_to_dict(articles: Iterable[Movies]):
#    return [movie_to_dict(movie) for movie in movies]


def comment_to_dict(review: Review):
    comment_dict = {
        'username': review.user.user_name,
        'article_id': review.movie,
        'comment_text': review.review_text,
        'timestamp': review.timestamp
    }
    return comment_dict


def comments_to_dict(comments: Iterable[Review]):
    return [comment_to_dict(rev) for rev in comments]

"""
def tag_to_dict(tag: Tag):
    tag_dict = {
        'name': tag.tag_name,
        'tagged_articles': [article.id for article in tag.tagged_articles]
    }
    return tag_dict


def tags_to_dict(tags: Iterable[Tag]):
    return [tag_to_dict(tag) for tag in tags]


# ============================================
# Functions to convert dicts to model entities
# ============================================

def dict_to_article(dict):
    article = Article(dict.id, dict.date, dict.title, dict.first_para, dict.hyperlink)
    # Note there's no comments or tags.
    return article
"""