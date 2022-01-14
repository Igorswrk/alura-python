import sys

class User:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


class Bidding:

    def __init__(self, user, value):
        self.user = user
        self.value = value


class Auction:

    def __init__(self, description):
        self.description = description
        self.__biddings = []

    @property
    def biddings(self):
        return self.__biddings


class Evaluator:

    def __init__(self):
        self.highest_bidding = sys.float_info.min
        self.lowest_bidding = sys.float_info.max

    def evaluate(self, auction:Auction):
        for i in auction.biddings:
            if i.value > self.highest_bidding:
                self.highest_bidding = i.value
            if i.value < self.lowest_bidding:
                self.lowest_bidding = i.value
