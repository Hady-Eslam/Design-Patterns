from Client import Client
from Services import ExampleService, NoService, PrintService


exampleService = ExampleService()
noService = NoService()
printService = PrintService()


client = Client(exampleService)
client.Print()

client.SetService(noService)
client.Print()

client.SetService(printService)
client.Print()
