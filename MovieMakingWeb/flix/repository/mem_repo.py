import csv
import os
from datetime import date, datetime
from typing import List

from bisect import bisect, bisect_left, insort_left

from werkzeug.security import generate_password_hash
from flix.repository.repo import AbstractRepository, RepositoryException
from flix.domainmodel.model import Director,Genre,Actor,Movie,Review,User, WatchList
import flix.repository.repo as repo

class MemoryRepository(AbstractRepository):

    def __init__(self):
        self._movie = list()
        self._genre = list()
        self._actors = list()
        self._directors = list()
        self.user = list()
        self._review = dict()
        self._watchlst = dict()

    def add_watchlst(self, username, movie):
        if username not in self._watchlst:
            self._watchlst[username] = [movie]
        else:
            if movie not in self._watchlst[username]:
                self._watchlst[username].append(movie)

    def get_watchlst(self, username):
        movies_ret = list()
        if username in self._watchlst:
            for mov in self._watchlst[username]:
                movies_ret.append(mov)
        return movies_ret

    def remove_from_watchlist(self, username, movie):
        if movie in self._watchlst[username]:
            mov_i = self._watchlst[username].index(movie)
            if mov_i != -1:
                self._watchlst[username].pop(mov_i)
        return self.get_watchlst(username)

    def add_user(self, user: User):
        self.user.append(user)

    def get_user(self, username) -> User:
        for user in self.user:
            if user.user_name == username:
                return user
        return None


    def add_director(self, director: Director):
        self._directors.append(director)

    def get_director(self):
        return next((director for director in self._directors), None)

    def add_actor(self, actor: Actor):
        self._actors.append(actor)

    def get_actor(self) -> Actor:
        return next((actor for actor in self._actors), None)

    def add_movie(self, movie : Movie):
        insort_left(self._movie, movie)

    def add_genre(self, genre: Genre):
        self._genre.append(genre)

    def get_genre(self) -> List[Genre]:
        return next((genre for genre in self._genre), None)

    def get_genre_lst(self):
        return self._genre

    def get_movie(self, movie : str):
        for mov in self._movie:
            if mov.title == movie:
                return mov

        return None

    def get_movie_by_year(self, year) -> List[Movie]:
        matching_movie = list()
        for movie in self._movie:
            if movie.year == year:
                matching_movie.append(movie)
            else:
                break

        return matching_movie
    def get_movie_for_genre(self, genre_name: str):
        genre = next((gen for gen in self._genre if gen.genre_name == genre_name), None)

        # Retrieve the ids of articles associated with the Tag.
        if genre is not None:
            mov_dct = get_movies_by("flix/datafiles", "genre")
            movies_gen = [movie for movie in mov_dct[genre]]
        else:
            # No Tag with name tag_name, so return an empty list.
            movies_gen = list()

        return movies_gen

    def get_number_of_movies(self):
        return len(self._movie)

    def get_first_movie(self):
        movie = None

        if len(self._movie) > 0:
            movie = self._movie[0]
        return movie

    def get_last_movie(self):
        movie = None

        if len(self._movie) > 0:
            movie = self._movie[-1]
        return movie

    def get_selected_movies(self, index_lst):
        selected_mov = list()
        for i in index_lst:
            selected_mov.append(self._movie[i])
        return selected_mov

    def add_review(self, movie: str, review: str, username: str):
        if username == None:
            raise RepositoryException

        if movie in self._review:
            self._review[movie] += [[review, username]]
        else:
            self._review[movie] = [[review, username]]

    def get_review(self, movie:str):
        comments = list()
        if self._review[movie] != []:
            for e in self._review[movie]:
                comments.append(e)
        return comments

    def get_review_lst(self):
        return self._review

def read_csv_file(filename: str):
    with open(filename, mode='r', encoding='utf-8-sig') as csvfile:
        movie_file_reader = csv.reader(csvfile)

        # Read first line of the the CSV file.
        headers = next(movie_file_reader)

        # Read remaining rows from the CSV file.
        for row in movie_file_reader:
            # Strip any leading/trailing white space from data read.
            row = [item.strip() for item in row]
            yield row
    return movie_file_reader

def load_movies(data_path: str, repo: MemoryRepository):
    dataset_of_movies = []
    dataset_of_actors = []
    dataset_of_directors = []
    dataset_of_genres = []

    all_act = []
    all_dir = []
    all_gen = []

    file = read_csv_file(os.path.join(data_path, 'Data1000Movies.csv'))
    for row in file:
        title = row[1]
        title = title.strip()
        release_year = int(row[6])
        mov = Movie(title, release_year)
        repo.add_movie(mov)
        dataset_of_movies += [mov]

        actors = row[5]
        actors = actors.split(",")
        for a in actors:
            a = a.strip()
            actor = Actor(a)
            if a not in all_act:
                all_act.append(a)
                repo.add_actor(actor)
                dataset_of_actors.append(actor)

        director = row[4]
        director = director.strip()
        d = Director(director)
        if director not in all_dir:
            all_dir.append(director)
            repo.add_director(d)
            dataset_of_directors += [d]

        genre = row[2]
        genre = genre.split(",")
        for g in genre:
            g = g.strip()
            gen = Genre(g)
            if g not in all_gen:
                all_gen.append(g)
                repo.add_genre(gen)
                dataset_of_genres.append(gen)

def populate(data_path: str, repo: MemoryRepository):
    load_movies(data_path, repo)

def get_movies_by(data_path: str, chosen_dict = None):
    genre_dict = dict()
    actor_dict = dict()
    director_dict = dict()
    movie_dict = dict()

    dataset_of_movies = []
    dataset_of_actors = []
    dataset_of_directors = []
    dataset_of_genres = []

    all_act = []
    all_dir = []
    all_gen = []

    file = read_csv_file(os.path.join(data_path, 'Data1000Movies.csv'))
    for row in file:
        title = row[1]
        title = title.strip()
        release_year = int(row[6])
        mov = Movie(title, release_year)
        dataset_of_movies += [mov]

        actors = row[5]
        actors = actors.split(",")
        for a in actors:
            a = a.strip()
            actor = Actor(a)
            if a not in all_act:
                all_act.append(a)
                dataset_of_actors.append(actor)
                actor_dict[a] = list()
            actor_dict[a].append(mov)

        director = row[4]
        director = director.strip()
        d = Director(director)
        if director not in all_dir:
            all_dir.append(director)
            dataset_of_directors += [d]
            director_dict[director] = list()
        director_dict[director].append(mov)

        genre = row[2]
        genre = genre.split(",")
        for g in genre:
            g = g.strip()
            gen = Genre(g)
            if g not in all_gen:
                all_gen.append(g)
                dataset_of_genres.append(gen)
                genre_dict[g] = list()
            genre_dict[g].append(mov)

    if chosen_dict == "genre":
        return genre_dict
    if chosen_dict == "actor":
        return actor_dict
    if chosen_dict == "movie":
        return dataset_of_movies

def get_all_genre():
    get_gen_lst = get_movies_by("flix/datafiles", "genre")
    return get_gen_lst.keys()

def get_all_movies():
    get_all = get_movies_by("flix/datafiles", "movie")
    return get_all

def get_all_movies_titles():
    get_all = get_movies_by("flix/datafiles", "movie")
    return get_all

def get_all_actors():
    get_actors = get_movies_by("flix/datafiles", "actor")
    return get_actors.keys()
