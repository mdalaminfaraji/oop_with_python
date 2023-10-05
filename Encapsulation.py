class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name=holder_name
        self.__balance=initial_deposit
        self._branch="bannani"
    
    def deposit(self, amount):
        self.__balance+=amount
    def get_balance(self):
        return self.__balance

rafsun=Bank('Chooto bro', 10000)

print(rafsun.holder_name)

print(rafsun.get_balance())
print(rafsun._branch)