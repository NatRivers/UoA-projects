#from domainmodel.genre import Genre
#from domainmodel.actor import Actor
#from domainmodel.director import Director

class Movie:
    def __init__(self, movie = "", year = int()):
        if movie != "" and type(movie) == str:
            movie = movie.strip()
            self.__title = movie
        if year >= 1900:
            self.__year = year
        self.__description = ""
        self.director = Director()
        self.actors = []
        self.genres = []
        self.runtime_minutes = int()

    def __setattr__(self, name, val):
        self.__dict__[name] = val
        print(self.__dict__)
        if 'description' in self.__dict__:
            self.__dict__['description'] = self.__dict__['description'].strip()
        if 'runtime_minutes' in self.__dict__:
            if self.__dict__['runtime_minutes'] < 0:
                raise ValueError("Constraint: the runtime is a positive number")
        
    def __repr__(self):
        return "<Movie " + self.__title + ", " + str(self.__year) + ">"

    def __eq__(self, other):
        s = self.__title.lower() + str(self.__year)
        o = other.__title.lower() + str(other.__year)
        return s == o
        
    def __lt__(self, other):
        s = self.__title.lower() + str(self.__year)
        o = other.__title.lower() + str(other.__year)
        return s < o
        
    def __hash__(self):
        s = self.__title.lower() + str(self.__year)
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

movie = Movie("Moana", 2016)
print(movie)

director = Director("Ron Clements")
movie.director = director
print(movie.director)

actors = [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
for actor in actors:
    movie.add_actor(actor)
print(movie.actors)
actors = [Actor("a"), Actor("b")]
for actor in actors:
    movie.add_actor(actor)
print(movie.actors)

movie.runtime_minutes = 107
print("Movie runtime: {} minutes".format(movie.runtime_minutes))
