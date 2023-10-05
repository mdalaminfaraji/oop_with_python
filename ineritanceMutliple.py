class Family:
    def __init__(self, memberQuantity) -> None:
        self.memberQuantity=memberQuantity
class School:
    def __init__(self, level, id) -> None:
        self.level=level
        self.id=id
class Sports:
    def __init__(self, game) -> None:
        self.game=game

class Student(Family, School, Sports):
    def __init__(self, memberQuantity, address, id, level, game) -> None:
        School.__init__(self, id, level)
        Sports.__init__(self, game)
        self.address=address
        super().__init__(memberQuantity)