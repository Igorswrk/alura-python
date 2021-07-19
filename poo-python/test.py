def create_account(number, user, balance, limit):
    account = {"number": number, "user": user, "balance": balance, "limit": limit}
    return account


def deposit(account, value):
    account["balance"] += value


def withdraw(account, value):
    account["balance"] -= value


def statement(account):
    print(f'balance {account["balance"]}')



