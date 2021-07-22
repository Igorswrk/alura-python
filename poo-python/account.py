class Account:
    def __init__(self, number, user, balance, limit):
        print(f'building object {self}')
        self.__number = number  # Atributos
        self.__user = user
        self.__balance = balance
        self.__limit = limit

    def deposit(self, value):
        self.__balance += value

    def withdraw(self, value):
        self.__balance -= value

    def statement(self):
        print(f"balance {self.__balance} of the user {self.__user}")

    def transfer(self, value, destiny_account):
        self.withdraw(value)
        destiny_account.deposit(value)
