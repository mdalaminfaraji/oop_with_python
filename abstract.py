from abc import ABC, abstractmethod

#abstract base class

class Animal(ABC):
    @abstractmethod #enforce all derived class to have a eat method
    def eat(self):
        print("I need food")
    @abstractmethod
    def move(self):
        pass
class Monkey(Animal):
    def __init__(self, name) -> None:
        self.category='Monkey'
        self.name = name
        super().__init__()

layka=Monkey('lucky')
layka.eat()