from datetime import date

import pytest

from flix.authentication.services import AuthenticationException
from flix.movies import services as movs_services
from flix.authentication import services as auth_services
from flix.movies.services import NonExistentMovieException


def test_can_add_user(in_memory_repo):
    new_username = 'jz'
    new_password = 'abcd1A23'

    auth_services.add_user(new_username, new_password, in_memory_repo)

    user_as_dict = auth_services.get_user(new_username, in_memory_repo)
    assert user_as_dict['username'] == new_username

    # Check that password has been encrypted.
    assert user_as_dict['password'].startswith('pbkdf2:sha256:')


def test_cannot_add_user_with_existing_name(in_memory_repo):
    username = 'thorke'
    password = 'abcd1A23'
    auth_services.add_user(username, password, in_memory_repo)

    with pytest.raises(auth_services.NameNotUniqueException):
        auth_services.add_user(username, password, in_memory_repo)


def test_authentication_with_valid_credentials(in_memory_repo):
    new_username = 'pmccartney'
    new_password = 'abcd1A23'

    auth_services.add_user(new_username, new_password, in_memory_repo)

    try:
        auth_services.authenticate_user(new_username, new_password, in_memory_repo)
    except AuthenticationException:
        assert False


def test_authentication_with_invalid_credentials(in_memory_repo):
    new_username = 'pmccartney'
    new_password = 'abcd1A23'

    auth_services.add_user(new_username, new_password, in_memory_repo)

    with pytest.raises(auth_services.AuthenticationException):
        auth_services.authenticate_user(new_username, '0987654321', in_memory_repo)


def test_can_add_comment(in_memory_repo):
    new_username = 'pmccartney'
    new_password = 'abcd1A23'

    auth_services.add_user(new_username, new_password, in_memory_repo)

    movie_title = '21'
    comment_text = 'The loonies are stripping the supermarkets bare!'
    username = 'pmccartney'

    # Call the service layer to add the comment.
    movs_services.add_review(movie_title, comment_text, username, in_memory_repo)

    # Retrieve the comments for the article from the repository.
    comments_as_dict = movs_services.get_reviews_for_movie(movie_title, in_memory_repo)

    # Check that the comments include a comment with the new comment text.
    assert comments_as_dict != []


def test_cannot_add_comment_for_non_existent_movie(in_memory_repo):
    new_username = 'pmccartney'
    new_password = 'abcd1A23'
    auth_services.add_user(new_username, new_password, in_memory_repo)

    mov_title = 'abcsac'
    comment_text = "what's that movie?"
    username = 'pmccartney'

    # Call the service layer to attempt to add the comment.
    with pytest.raises(movs_services.NonExistentMovieException):
        movs_services.add_review(mov_title, comment_text, username, in_memory_repo)


def test_cannot_add_comment_by_unknown_user(in_memory_repo):
    mov_title = '21'
    comment_text = 'The loonies are stripping the supermarkets bare!'
    username = 'gmichael'

    # Call the service layer to attempt to add the comment.
    with pytest.raises(movs_services.UnknownUserException):
        movs_services.add_review(mov_title, comment_text, username, in_memory_repo)


def test_get_comments_for_non_existent_movie(in_memory_repo):
    assert movs_services.get_reviews_for_movie('abcsd', in_memory_repo) == []


def test_get_comments_for_movie_without_comments(in_memory_repo):
    comments_as_dict = movs_services.get_reviews_for_movie('21', in_memory_repo)
    assert len(comments_as_dict) == 0