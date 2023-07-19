import abc
from abc import ABC

class Fruit(ABC):
    @abc.abstractmethod
    def tam(self):
        pass
class Mango(Fruit):
    def tam(self):
        pass
class Banan(Fruit):
    def tam(self):
        pass

obj=Mango()
print(obj)

