class House:
    def __init__(self, name, price, flat) -> None:
        self.name=name
        self.price=price
        self.flat=flat
    def __repr__(self) -> str:
        return f'home name {self.name} flat quantity {self.flat} flat price {self.flat}'

class Varite(House):
    def __init__(self, name, price, flat, mobile) -> None:
        self.mobile=mobile
        super().__init__(name, price, flat)
    def __repr__(self) -> str:
        print(f'mobile number: {self.mobile}')
        return super().__repr__()
    
class Gard(Varite):
    def __init__(self, name, price, flat, mobile, duty) -> None:
        self.duty=duty
        super().__init__(name, price, flat, mobile)
    def __repr__(self) -> str:
        print(f'duty :{self.duty}')
        return super().__repr__()

rohim =Gard('dhaka house', 9877, '2nd', '2346286748', 'morning')
print(rohim)