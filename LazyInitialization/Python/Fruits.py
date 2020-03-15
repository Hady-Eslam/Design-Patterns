class Fruit:
    def __init__(self, Name):
        self.Name = Name
    
    def __str__(self):
        return self.Name

class Fruits:

    def __init__(self):
        self.__Fruits = {}

    def GetFruit(self, Name):
        if Name not in self.__Fruits:
            self.__Fruits[Name] = Fruit(Name)
        return self.__Fruits[Name]
    
    def PrintFruits(self):
        for Name in self.__Fruits:
            print(Name)
        
        print('_______________')
