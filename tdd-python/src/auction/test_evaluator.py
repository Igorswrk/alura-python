from unittest import TestCase

from src.auction.domain import Bidding, Auction, User, Evaluator


class TestEvaluator(TestCase):

    def setUp(self):
        self.igor = User('igor')
        self.bidding_igor = Bidding(self.igor, 150.0)
        self.auction = Auction('Celular')

    def create_auction(self):
        pass

    def create_evaluator(self):
        pass

    def test_should_return_the_highest_and_lowest_biddings_when_added_in_ascending_order(self):
        amanda = User('amanda')
        bidding_amanda = Bidding(amanda, 150.0)

        self.auction.biddings.append(self.bidding_igor)
        self.auction.biddings.append(bidding_amanda)

        evaluator = Evaluator()
        evaluator.evaluate(self.auction)

        lowest_expected_value = 100.0
        highest_expected_value = 150.0

        self.assertEqual(lowest_expected_value, evaluator.lowest_bidding)
        self.assertEqual(highest_expected_value, evaluator.highest_bidding)

    def test_should_return_the_highest_and_lowest_biddings_when_added_in_descending_order(self):
        amanda = User('amanda')
        bidding_amanda = Bidding(amanda, 150.0)

        self.auction.biddings.append(bidding_amanda)
        self.auction.biddings.append(self.bidding_igor)

        evaluator = Evaluator()
        evaluator.evaluate(self.auction)

        lowest_expected_value = 100.0
        highest_expected_value = 150.0

        self.assertEqual(lowest_expected_value, evaluator.lowest_bidding)
        self.assertEqual(highest_expected_value, evaluator.highest_bidding)

    def test_should_return_the_same_value_for_highest_and_lowest_bidding_when_auction_has_only_one_bidding(self):
        self.auction.biddings.append(self.bidding_igor)

        evaluator = Evaluator()
        evaluator.evaluate(self.auction)

        self.assertEqual(150.0, evaluator.lowest_bidding)
        self.assertEqual(150.0, evaluator.highest_bidding)

    def test_should_return_the_same_value_for_highest_and_lowest_bidding_when_auction_has_only_three_bidding(self):
        amanda = User('amanda')
        mel = User('mel')

        bidding_amanda = Bidding(amanda, 150.0)
        bidding_mel = Bidding(mel, 200.0)

        self.auction.biddings.append(bidding_amanda)
        self.auction.biddings.append(bidding_mel)
        self.auction.biddings.append(self.bidding_igor)

        evaluator = Evaluator()
        evaluator.evaluate(self.auction)

        lowest_expected_value = 100.0
        highest_expected_value = 200.0

        self.assertEqual(lowest_expected_value, evaluator.lowest_bidding)
        self.assertEqual(highest_expected_value, evaluator.highest_bidding)
