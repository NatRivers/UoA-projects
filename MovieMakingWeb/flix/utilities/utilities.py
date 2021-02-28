from flask import Blueprint, request, render_template, redirect, url_for, session

import flix.repository.repo as repo
import flix.utilities.services as services
import flix.repository.mem_repo as mem_repo

# Configure Blueprint.
utilities_blueprint = Blueprint(
    'utilities_bp', __name__)

def choose_selected_movies(quantity=3):
    mov = services.get_random_movies(quantity, repo.repo_instance)
    print(mov)
    return mov

def get_movies_with_genre():
    movies_genre = dict()
    movies_in_genre = sorted(mem_repo.get_all_genre())
    for gen in movies_in_genre:
        movies_genre[gen] = url_for('movies_bp.movies_by_genre', genre=gen)

    return movies_genre

def get_movies_with_actor():
    movies_actor = dict()
    movies_in_actors = sorted(mem_repo.get_all_actors())
    for actor in movies_in_actors:
        movies_actor[actor] = url_for('movies_bp.movies_by_actor', actor=actor)

    return movies_actor

def get_movies_all():
    movies_dict = dict()
    movies_all = sorted(mem_repo.get_all_movies_titles())
    for movie in movies_all:
        movies_dict[movie.title] = url_for('movies_bp.comment_on_movies', movie=movie.title)

    return movies_dict