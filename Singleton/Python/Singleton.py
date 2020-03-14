class MetaSingleton:

    def __init__(self, The_Singleton):
        self.__Singleton = The_Singleton()
    
    def __call__(self, Value):
        return self.__Singleton

@MetaSingleton
class Singleton:

    def do_some_things(self):
        pass
