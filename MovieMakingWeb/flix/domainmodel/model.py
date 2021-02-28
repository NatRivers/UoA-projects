import csv
import datetime


class Director:  ##1
    def __init__(self, director_full_name = ""):
        if director_full_name == "" or type(director_full_name) is not str:
            self.director_full_name = "None"
        else:
            self.director_full_name = director_full_name.strip()

    def __repr__(self):
        return "<Director " + self.director_full_name  + ">"

    def __eq__(self, other):
        return self.director_full_name == other.director_full_name

    def __lt__(self, other):
        return self.director_full_name < other.director_full_name

    def __hash__(self):
        return hash(self.director_full_name)


class Genre: ##2
    def __init__(self, genre_name = ""):
        self.genre_lst = []
        if genre_name == "" or type(genre_name) != str:
            self.genre_name = "None"
        else:
            self.genre_name = genre_name.strip()
            if self.genre_name not in self.genre_lst:
                self.genre_lst.append(self.genre_name)

    def __repr__(self):
        if self.genre_name == "":
            self.genre_name = "None"
        return "<Genre " + self.genre_name  + ">"
        
    def __eq__(self, other):
        return self.genre_name == other.genre_name
        
    def __lt__(self, other):
        return self.genre_name < other.genre_name
        
    def __hash__(self):
        return hash(self.genre_name)

class Actor: ##3
    def __init__(self, name = ""):
        self.actor_full_name = name
        if self.actor_full_name == "" or type(self.actor_full_name) != str:
            self.actor_full_name = "None"
        else:
            self.actorlst = []
        
    def __repr__(self):
        return "<Actor " + self.actor_full_name  + ">"
        
    def __eq__(self, other):
        return self.actor_full_name == other.actor_full_name
        
    def __lt__(self, other):
        return self.actor_full_name < other.actor_full_name
        
    def __hash__(self):
        return hash(self.actor_full_name)
    
    def add_actor_colleague(self, colleague):
        self.actorlst += [colleague]
        
    def check_if_this_actor_worked_with(self, colleague):
        return colleague in self.actorlst

class Movie: ##4
    def __init__(self, movie = "", year = int()):
        if movie != "" and type(movie) == str:
            movie = movie.strip()
            self.title = movie
        if year >= 1900:
            self.year = year
        self.description = ""
        self.director = Director()
        self.actors = []
        self.genres = []
        self.review = []
        self.runtime_minutes = int()
        self.view_comment_url = str()
        self.add_comment_url = str()
        self.watchlst_url = str()
        self.removemov_watchlst = str()

    def __setattr__(self, name, val):
        self.__dict__[name] = val
##        print(self.__dict__)
        if 'description' in self.__dict__:
            self.__dict__['description'] = self.__dict__['description'].strip()
        if 'runtime_minutes' in self.__dict__:
            if self.__dict__['runtime_minutes'] < 0:
                raise ValueError("Constraint: the runtime is a positive number")
        
    def __repr__(self):
        return "<Movie " + self.title + ", " + str(self.year) + ">"

    def __eq__(self, other):
        s = self.title.lower() + str(self.year)
        o = other.title.lower() + str(other.year)
        return s == o
        
    def __lt__(self, other):
        s = self.title.lower() + str(self.year)
        o = other.title.lower() + str(other.year)
        return s < o
        
    def __hash__(self):
        s = self.title.lower() + str(self.year)
        return hash(s)

    def add_actor(self, actor):
        self.actors.append(actor)

    def remove_actor(self, actor):
        try:
            self.actors.index(actor)
            self.actors.pop(self.actors.index(actor))
        except ValueError:
            pass
                   
    def add_genre(self, genre): 
        self.genres.append(genre)

    def remove_genre(self, genre):
        try:
            self.genres.index(genre)
            self.genres.pop(self.genres.index(genre))
        except ValueError:
            pass

    def add_review(self, review):
        self.review.append(review)

    def view_url(self, url):
        self.view_comment_url = url
    def add_url(self, url):
        self.add_comment_url = url

    def add_watchlst_url(self, url):
        self.watchlst_url = url

    def remove_url(self, url):
        self.remove_watchlst_url = url

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

class User:  ##7
    def __init__(self, username=str(), pw=str()):
        self.user_name = username.strip().lower()
        self.password = pw
        self.watched_movies = []
        self.reviews = []
        self.time_spent_watching_movies_minutes = int()

    def __repr__(self):
        return "<User " + self.user_name + ">"

    def __eq__(self, other):
        return self.user_name == other.user_name

    def __lt__(self, other):
        return self.user_name < other.user_name

    def __hash__(self):
        return hash(self.user_name)

    def watch_movie(self, movie):
        if movie not in self.watched_movies:
            self.watched_movies.append(movie)
        self.time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if review not in self.reviews:
            self.reviews.append(review)

class Review: ##6
    def __init__(self, user = User, movie = Movie(), review_text = "", rating = 1):
        self.user = user
        self.movie = movie
        self.review_text = review_text.strip()
        self.timestamp = datetime.datetime.today()
        if type(rating) == int and rating >= 1 and rating <= 10:
            self.rating = rating
        else:
            self.rating = None

    def __repr__(self):
        return str(self.movie) + ", Review: " + str(self.review_text) + ", Rating: " + str(self.rating) + ", Time: " + str(self.timestamp)

    def __eq__(self, other):
        s = str(self.movie).lower() + self.review_text.lower() + str(self.rating) + str(self.timestamp)
        o = str(other.movie).lower() + other.review_text.lower() + str(other.rating) + str(other.timestamp)
        return  s == o

class WatchList: #8
    def __init__(self):
        self.watch_list = []

    def add_movie(self, movie):
        if movie not in self.watch_list:
            self.watch_list.append(movie)

    def remove_movie(self, movie):
        try:
            i = self.watch_list.index(movie)
            self.watch_list.pop(i)
        except ValueError:
            pass

    def select_movie_to_watch(self, index):
        lst_len = self.size()
        if index >= lst_len:
            return None
        return self.watch_list[index]

    def size(self):
        return len(self.watch_list)

    def first_movie_in_watchlist(self):
        lst_len = self.size()
        if lst_len > 0:
            return self.watch_list[0]
        return None

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        lst_len = self.size()
        if self.i < lst_len:
            m = self.watch_list[self.i]
            self.i += 1
            return m
        else:
            raise StopIteration()

def make_review(comment_text: str, user: User, movie: str, timestamp: datetime = datetime.datetime.today()):
    comment = Review(comment_text, movie)
    comment.timestamp = timestamp
    user.add_review(comment)
    movie.add_review(comment)

    return comment
