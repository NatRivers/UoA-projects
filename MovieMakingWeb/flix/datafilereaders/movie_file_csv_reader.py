import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director

class MovieFileCSVReader:
    def __init__(self, filename):
        self.__file_name = filename
        self.dataset_of_movies = []
        self.dataset_of_actors = []
        self.dataset_of_directors = []
        self.dataset_of_genres = []

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            all_act = []
            all_dir = []
            all_gen = []
            for row in movie_file_reader:
                title = row['Title']
                title = title.strip()
                release_year = int(row['Year'])
                mov = Movie(title, release_year)
                self.dataset_of_movies += [mov]

                actors = row['Actors']
                actors = actors.split(",")
                for a in actors:
                    a = a.strip()
                    actor = Actor(a)
                    if a not in all_act:
                        all_act.append(a)
                        self.dataset_of_actors.append(actor)

                director = row['Director']
                director = director.strip()
                d = Director(director)
                if director not in all_dir:
                    all_dir.append(director)
                    self.dataset_of_directors.append(d)

                genre = row['Genre']
                genre = genre.split(",")
                for g in genre:
                    g = g.strip()
                    gen = Genre(g)
                    if g not in all_gen:
                        all_gen.append(g)
                        self.dataset_of_genres.append(gen)
