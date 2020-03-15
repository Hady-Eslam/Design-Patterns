from Services import Service

class Client:

    def __init__(self, service : Service):
        self.__Service = service
    
    def SetService(self, service : Service):
        self.__Service = service
    
    def Print(self):
        self.__Service.Print()
