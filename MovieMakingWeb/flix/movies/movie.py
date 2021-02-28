from datetime import date

from flask import Blueprint
from flask import request, render_template, redirect, url_for, session

from better_profanity import profanity
from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

import flix.repository.repo as repo
import flix.repository.mem_repo as mem_repo
import flix.utilities.utilities as utilities
import flix.movies.services as services

from flix.authentication.authentication import login_required


# Configure Blueprint.
movies_blueprint = Blueprint(
    'movies_bp', __name__)

@movies_blueprint.route('/movies_by_genre', methods=['GET'])
def movies_by_genre():
    movies_per_page = 15
    gen_name = request.args.get('genre')
    cursor = request.args.get('cursor')
    movie_to_watchlst = request.args.get('movie')
    get_movies_dict = mem_repo.get_movies_by("flix/datafiles", "genre")
    chosen_movies = sorted(get_movies_dict[gen_name])
    comments = request.args.get('view_comments_for')

    if comments == None:
        comments = "None"

    if movie_to_watchlst == None:
        movie_to_show_comments = "None"
    else:
        username = session['username']
        for mov in chosen_movies:
            if mov.title == movie_to_watchlst[movie_to_watchlst.find(" ") + 1: movie_to_watchlst.find(",")]:
                mov.remove_url(url_for('movies_bp.my_watchlst', movie=mov))
                services.add_to_watchlist(username, mov, repo.repo_instance)

    if cursor is None:
        # No cursor query parameter, so initialise cursor to start at the beginning.
        cursor = 0
    else:
        # Convert cursor from string to int.
        cursor = int(cursor)
    movs_to_show = chosen_movies[cursor:cursor + movies_per_page]

    next_mov_url = None
    prev_mov_url = None

    if cursor > 0:
        prev_mov_url = url_for('movies_bp.movies_by_genre', genre=gen_name, cursor=cursor - movies_per_page)

    if cursor + movies_per_page < len(chosen_movies):
        # There are further articles, so generate URLs for the 'next' and 'last' navigation buttons.
        next_mov_url = url_for('movies_bp.movies_by_genre', genre=gen_name, cursor=cursor + movies_per_page)

    for movie in chosen_movies:
        movie.view_url(url_for('movies_bp.movies_by_genre', genre=gen_name, cursor=cursor, view_comments_for=movie))
        movie.add_url(url_for('movies_bp.comment_on_movies', movie = movie))
        movie.add_watchlst_url(url_for('movies_bp.movies_by_genre', genre=gen_name, cursor=cursor, movie=movie))

    reviews_for_mov = ""
    if comments != None:
        reviews_for_mov = services.get_reviews_for_movie(comments[comments.find(" ") + 1: comments.find(",")],
                                                         repo.repo_instance)

    return render_template(
        'movies/movies.html',
        movies_title='Movies with genre: ' + gen_name,
        movies=movs_to_show,
        prev_mov_url=prev_mov_url,
        next_mov_url=next_mov_url,
        mov_gen=utilities.get_movies_with_genre(),
        genre_display=utilities.get_movies_with_genre(),
        see_comments=comments[comments.find(" ") + 1: comments.find(",")],
        mov_rev='Reviews for Movie: ' + comments[comments.find(" ") + 1: comments.find(",")],
        comment_for_movie=reviews_for_mov
    )

@movies_blueprint.route('/movies', methods=['GET'])
def display_all_movies():
    all_movies = sorted(mem_repo.get_all_movies())
    cursor = request.args.get('cursor')
    movies_per_page = 15
    movie_to_watchlst = request.args.get('movie')
    comments = request.args.get('view_comments_for')

    if movie_to_watchlst == None:
        movie_to_watchlst = "None"
    else:
        username = session['username']
        for mov in all_movies:
            if mov.title == movie_to_watchlst[movie_to_watchlst.find(" ") + 1 : movie_to_watchlst.find(",")]:
                mov.remove_url(url_for('movies_bp.my_watchlst', movie=mov))
                services.add_to_watchlist(username, mov, repo.repo_instance)
    if comments == None:
        comments = "None"

    if cursor is None:
        # No cursor query parameter, so initialise cursor to start at the beginning.
        cursor = 0
    else:
        # Convert cursor from string to int.
        cursor = int(cursor)

    movs_to_show = all_movies[cursor:cursor + movies_per_page]

    next_mov_url = None
    prev_mov_url = None

    if cursor > 0:
        prev_mov_url = url_for('movies_bp.display_all_movies', cursor=cursor - movies_per_page)

    if cursor + movies_per_page < len(all_movies):
        # There are further articles, so generate URLs for the 'next' and 'last' navigation buttons.
        next_mov_url = url_for('movies_bp.display_all_movies', cursor=cursor + movies_per_page)

    for movie in all_movies:
        movie.view_url(url_for('movies_bp.display_all_movies', view_comments_for=movie, cursor=cursor))
        movie.add_url(url_for('movies_bp.comment_on_movies', movie=movie))
        movie.add_watchlst_url(url_for('movies_bp.display_all_movies', cursor=cursor, movie=movie))

    reviews_for_mov = ""
    if comments != None:
        reviews_for_mov = services.get_reviews_for_movie(comments[comments.find(" ") + 1 : comments.find(",")], repo.repo_instance)

    return render_template(
        'movies/movies.html',
        movies=movs_to_show,
        prev_mov_url = prev_mov_url,
        next_mov_url = next_mov_url,
        movies_title='All Movies',
        genre_display=utilities.get_movies_with_genre(),
        see_comments = comments[comments.find(" ") + 1 : comments.find(",")],
        mov_rev = 'Reviews for Movie: ' + comments[comments.find(" ") + 1 : comments.find(",")],
        comment_for_movie = reviews_for_mov
    )

@movies_blueprint.route('/movies_by_actor', methods=['GET'])
def movies_by_actor():
    movie_to_watchlst = request.args.get('movie')
    act_name = request.args.get('actor')
    cursor = request.args.get('cursor')
    movies_per_page = 15
    comments = request.args.get('view_comments_for')

    get_movies_dict = mem_repo.get_movies_by("flix/datafiles", "actor")
    chosen_movies = sorted(get_movies_dict[act_name])

    if comments == None:
        comments = "None"

    if movie_to_watchlst == None:
        movie_to_show_comments = "None"
    else:
        username = session['username']
        for mov in chosen_movies:
            if mov.title == movie_to_watchlst[movie_to_watchlst.find(" ") + 1: movie_to_watchlst.find(",")]:
                mov.remove_url(url_for('movies_bp.my_watchlst', movie=mov))
                services.add_to_watchlist(username, mov, repo.repo_instance)

    if cursor is None:
        # No cursor query parameter, so initialise cursor to start at the beginning.
        cursor = 0
    else:
        # Convert cursor from string to int.
        cursor = int(cursor)

    movs_to_show = chosen_movies[cursor:cursor + movies_per_page]

    next_mov_url = None
    prev_mov_url = None

    if cursor > 0:
        prev_mov_url = url_for('movies_bp.movies_by_actor', actor=act_name, cursor=cursor - movies_per_page)

    if cursor + movies_per_page < len(chosen_movies):
        # There are further articles, so generate URLs for the 'next' and 'last' navigation buttons.
        next_mov_url = url_for('movies_bp.movies_by_actor', actor=act_name, cursor=cursor + movies_per_page)

    reviews_for_mov = ""
    if comments != None:
        reviews_for_mov = services.get_reviews_for_movie(comments[comments.find(" ") + 1: comments.find(",")],
                                                         repo.repo_instance)

    for movie in chosen_movies:
        movie.view_url(url_for('movies_bp.movies_by_actor', actor=act_name, view_comments_for=movie,cursor=cursor))
        movie.add_url(url_for('movies_bp.comment_on_movies', movie=movie))
        movie.add_watchlst_url(url_for('movies_bp.movies_by_actor', actor=act_name, cursor=cursor, movie=movie))

    return render_template(
        'movies/movies.html',
        movies_title='Movies by Actor: ' + act_name,
        movies=movs_to_show,
        prev_mov_url=prev_mov_url,
        next_mov_url=next_mov_url,
        genre_display=utilities.get_movies_with_genre(),
        mov_gen=utilities.get_movies_with_actor(),
        see_comments=comments[comments.find(" ") + 1: comments.find(",")],
        mov_rev='Reviews for Movie: ' + comments[comments.find(" ") + 1: comments.find(",")],
        comment_for_movie=reviews_for_mov
    )

@movies_blueprint.route('/comment', methods=['GET', 'POST'])
@login_required
def comment_on_movies():
    # Obtain the username of the currently logged in user.
    username = session['username']

    # Create form. The form maintains state, e.g. when this method is called with a HTTP GET request and populates
    # the form with an article id, when subsequently called with a HTTP POST request, the article id remains in the
    # form.
    form = CommentForm()
    movie_title = request.args.get('movie')

    if form.validate_on_submit():
        # Successful POST, i.e. the comment text has passed data validation.
        # Extract the article id, representing the commented article, from the form.
        movie_title = form.movie_title.data

        # Use the service layer to store the new comment.
        services.add_review(movie_title[movie_title.find(" ") + 1 :movie_title.find(",")], form.comment.data, username, repo.repo_instance)

        # Retrieve the article in dict form.
        movie_in_dict = services.get_movie(movie_title[movie_title.find(" ") + 1 :movie_title.find(",")], repo.repo_instance)

        # Cause the web browser to display the page of all articles that have the same date as the commented article,
        # and display all comments, including the new comment.
        return redirect(url_for('movies_bp.display_all_movies', view_comments_for=movie_title))

    if request.method == 'GET':
        # Request is a HTTP GET to display the form.
        # Extract the article id, representing the article to comment, from a query parameter of the GET request.
        movie_title = request.args.get('movie')

        # Store the article id in the form.
        form.movie_title.data = movie_title
    else:
        # Request is a HTTP POST where form validation has failed.
        # Extract the article id of the article being commented from the form.
        movie_title = form.movie_title.data

    # For a GET or an unsuccessful POST, retrieve the article to comment in dict form, and return a Web page that allows
    # the user to enter a comment. The generated Web page includes a form object.


    return render_template(
        'movies/movies_review.html',
        title='Edit article',
        movie=movie_title[movie_title.find(" ") + 1 :movie_title.find(",")],
        form=form,
        handler_url=url_for('movies_bp.comment_on_movies'),
        mov_gen = utilities.get_movies_all(),
        genre_display=utilities.get_movies_with_genre()
    )


class ProfanityFree:
    def __init__(self, message=None):
        if not message:
            message = u'Field must not contain profanity'
        self.message = message

    def __call__(self, form, field):
        if profanity.contains_profanity(field.data):
            raise ValidationError(self.message)


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', [
        DataRequired(),
        Length(min=4, message='Your comment is too short'),
        ProfanityFree(message='Your comment must not contain profanity')])
    movie_title = HiddenField("Movie Title")


@movies_blueprint.route('/watchlist', methods=['GET'])
def my_watchlst():
    username = session['username']
    movies = services.get_watchlist(username, repo.repo_instance)
    remove_mov = request.args.get('movie')

    for movie in movies:
        if remove_mov != None and movie.title == remove_mov[remove_mov.find(" ") + 1 : remove_mov.find(",")]:
            movies = services.remove_watchlst_movie(username, movie, repo.repo_instance)

    return render_template(
        'movies/watchlist.html',
        movies_title='My Watch List: ',
        movies=movies,
        genre_display=utilities.get_movies_with_genre(),
        mov_gen=utilities.get_movies_all()
    )
