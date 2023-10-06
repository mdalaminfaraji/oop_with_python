# poly-->many
# morph-->shape
class Animal:
    def __init__(self, name) -> None:
        self.name=name
    def make_sound(self):
        print('animal making some sound')
class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('meowe')
class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print("ghew")

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print("messi messsi")

cat=Cat("dogy")
cat.make_sound()
shepard=Dog('Local Shephared')
shepard.make_sound()

mess=Goat("L M")
mess.make_sound()

animals=[cat, shepard, mess]
for animal in animals:
    animal.make_sound()
