class Service:
    def Print(self):
        pass

class ExampleService(Service):
    def Print(self):
        print('Hello From Example Service')

class NoService(Service):
    def Print(self):
        print('Hello From No Service')

class PrintService(Service):
    def Print(self):
        print('Hello From Print Service')
