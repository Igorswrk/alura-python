class Account:
    def __init__(self, number, user, balance, limit):
        print(f'building object {self}')
        self.number = number  # Atributos
        self.user = user
        self.balance = balance
        self.limit = limit

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        self.balance -= value

    def statement(self):
        print(f"balance {self.balance} of the user {self.user}")

