class Genre:
    def __init__(self, genre_name = ""):
        if genre_name == "" or type(genre_name) != str:
            self.__genre_name = "None"
        else:
            self.__genre_name = genre_name.strip()
        
    def __repr__(self):
        if self.__genre_name == "":
            self.__genre_name = "None"
        return "<Genre " + self.__genre_name  + ">"
        
    def __eq__(self, other):
        return self.__genre_name == other.__genre_name
        
    def __lt__(self, other):
        return self.__genre_name < other.__genre_name
        
    def __hash__(self):
        return hash(self.__genre_name)
