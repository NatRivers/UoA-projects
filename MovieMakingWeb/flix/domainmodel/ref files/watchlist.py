#from domainmodel.movie import Movie

class WatchList:
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
