from Duck import Duck
from Bird import Bird

class DuckAdapter(Duck):

    def __init__(self, bird : Bird):
        self.__Bird  = bird
    
    def Squack(self):
        self.__Bird.MakeSound()
