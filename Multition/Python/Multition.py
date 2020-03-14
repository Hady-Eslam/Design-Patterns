from Classes import Class1, Class2, Class3

class Multition:

    __Pool = {
        'Class1' : None,
        'Class2' : None,
        'Class3' : None
    }

    @classmethod
    def GetInstance(cls, Type):
        if cls.__Pool[Type] is None:
            cls.__AddInstance(Type)
        return cls.__Pool[Type]
    
    @classmethod
    def __AddInstance(cls, Type):
        if Type == 'Class1':
            cls.__Pool['Class1'] = Class1()
        elif Type == 'Class2':
            cls.__Pool['Class2'] = Class2()
        else:
            cls.__Pool['Class3'] = Class3()
