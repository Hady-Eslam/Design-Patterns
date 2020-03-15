class Objecte:
    def __init__(self, Value):
        self.Value = Value

    def Print(self):
        print(self.Value)

class Pool:

    def __init__(self):
        self.__Pool = [
            Objecte(1),
            Objecte(2),
            Objecte(3),
        ]
    
    def GetObject(self):
        if len(self.__Pool) == 0:
            raise Exception('Pool is Busy')
        else:
            return self.__Pool.pop()
    
    def ReleaseObject(self, The_Object):
        self.__Pool.append(The_Object)
        del The_Object
