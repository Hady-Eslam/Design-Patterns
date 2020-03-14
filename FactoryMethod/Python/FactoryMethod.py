from Rooms import MagicRoom, OrdinaryRoom

class Game:
    
    def MakeRoom():
        pass

class MagicGame(Game):

    def MakeRoom(self):
        return MagicRoom()

class OrdinaryGame(Game):

    def MakeRoom(self):
        return OrdinaryRoom()
