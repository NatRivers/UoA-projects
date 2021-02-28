class Actor:
    def __init__(self, name = ""):
        self.__actor_full_name = name
        if self.__actor_full_name == "" or type(self.__actor_full_name) != str:
            self.__actor_full_name = "None"
        else:
            self.__actorlst = []
        
    def __repr__(self):
        return "<Actor " + self.__actor_full_name  + ">"
        
    def __eq__(self, other):
        return self.__actor_full_name == other.__actor_full_name
        
    def __lt__(self, other):
        return self.__actor_full_name < other.__actor_full_name
        
    def __hash__(self):
        return hash(self.__actor_full_name)
    
    def add_actor_colleague(self, colleague):
        self.__actorlst += [colleague]
        
    def check_if_this_actor_worked_with(self, colleague):
        return colleague in self.__actorlst