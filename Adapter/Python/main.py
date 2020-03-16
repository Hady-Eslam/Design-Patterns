from Bird import Sparrow
from Duck import BlackDuck
from Adapter import DuckAdapter

black_duck = BlackDuck()
black_duck.Squack()

sparrow = Sparrow()
sparrow.Fly()
sparrow.MakeSound()

adapter = DuckAdapter(sparrow)
adapter.Squack()
