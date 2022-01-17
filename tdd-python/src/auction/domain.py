import sys


class User:
    def __init__(self, name, wallet):
        self.__name = name
        self.__wallet = wallet

    @property
    def name(self):
        return self.__name

    @property
    def wallet(self):
        return self.__wallet

    def propose_bidding(self, auction, value):
        if value > self.__wallet:
            raise ValueError('Não pode propor um lance com valor maior que o valor da carteira')
        bidding = Bidding(self, value)
        auction.add_bidding(bidding)

        self.__wallet -= value

class Bidding:
    def __init__(self, user, value):
        self.user = user
        self.value = value


class Auction:
    def __init__(self, description):
        self.description = description
        self.__biddings = []
        self.highest_bidding = sys.float_info.min
        self.lowest_bidding = sys.float_info.max

    def add_bidding(self, bidding: Bidding):
        if not self.__biddings or self.__biddings[-1].user != bidding.user and bidding.value > self.__biddings[-1].value:
            if bidding.value > self.highest_bidding:
                self.highest_bidding = bidding.value
            if bidding.value < self.lowest_bidding:
                self.lowest_bidding = bidding.value

            self.__biddings.append(bidding)
        else:
            raise ValueError('Erro ao propor lance!')

    @property
    def biddings(self):
        return self.__biddings[:]
