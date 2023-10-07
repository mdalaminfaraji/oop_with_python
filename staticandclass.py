class Shopping:
    cart=[] #class attribute/or static attribute
    origin="china"

    def __init__(self, name, location) -> None:
        self.name=name #instance attribute
        self.location=location
    @staticmethod
    def multiply(a, b):
        result=a*b
        print(result)
    @classmethod
    def market(self, item):
        print(" mamam i " ,item)

dhaka=Shopping('sobuj ', 'london')
# dhaka.market('lingi')
# Shopping.multiply(23, 343)
dhaka.multiply(234, 23)
Shopping.market('sdj')