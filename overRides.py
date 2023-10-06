class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def eat(self):
        print(f'I eat rice {self.weight}')
class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team=team
        Person.__init__(self, name, age, height, weight)
    def eat(self):
        print(f'I eat rice ')
    
    def __add__(self, other):
        return self.age + other.age
    
    # * sign operator overload
    def __mul__(self, other):
        return self.weight * other.weight

    

mushi=Cricketer("mushi", 234, 234, 343434 , 'bd')
sakib=Cricketer("sakib", 234, 234, 343434 , 'bd')


print(sakib + mushi)
print(sakib * mushi)