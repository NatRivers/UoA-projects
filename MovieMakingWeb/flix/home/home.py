from flask import Blueprint, render_template

import flix.utilities.utilities as utilities
import flix.repository.mem_repo as mem_repo

home_blueprint = Blueprint(
    'home_bp', __name__)


@home_blueprint.route('/', methods=['GET'])
def home():
    return render_template(
        'home/home.html',
        selected_movies = utilities.choose_selected_movies(),
        selected_movies2=utilities.choose_selected_movies(),
        genre_display=utilities.get_movies_with_genre()
    )