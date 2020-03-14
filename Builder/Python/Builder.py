class Home:

    def __init__(self):
        self.__Parts = []

    def BuildGarden(self):
        self.__Parts.append('Garden')
    
    def BuildStatues(self):
        self.__Parts.append('Statues')
    
    def BuildSwimPool(self):
        self.__Parts.append('Swimpool')
    
    def BuildGarage(self):
        self.__Parts.append('Garage')
    
    def __str__(self):
        return str(self.__Parts)
