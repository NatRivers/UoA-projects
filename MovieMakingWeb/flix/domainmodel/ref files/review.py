#from datetime import datetime

#from domainmodel.movie import Movie

class Review:
    def __init__(self, movie = Movie(), review_text = "", rating = 1):
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
