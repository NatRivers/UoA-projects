from flask import Blueprint
from flask import request, render_template

import flix.repository.mem_repo as mem_repo
import flix.utilities.utilities as utilities

actors_blueprint = Blueprint(
    'actors_bp', __name__)

@actors_blueprint.route('/actors', methods=['GET'])
def show_all_actors():
    #all_actors = sorted(mem_repo.get_all_actors())
    return render_template(
        'movies/actors.html',
        actors = utilities.get_movies_with_actor(),
        genre_display=utilities.get_movies_with_genre()
    )