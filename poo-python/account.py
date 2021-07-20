
class Account:
    def __init__(self, number, user, balance, limit):
        print(f'construindo objeto {self}')
        self.number = number  # Atributos
        self.user = user
        self.balance = balance
        self.limit = limit
