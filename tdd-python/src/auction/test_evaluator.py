from unittest import TestCase

from src.auction.domain import Bidding, Auction, User, Evaluator


class TestEvaluator(TestCase):
    def test_evaluate(self):
        igor = User('igor')
        amanda = User('amanda')

        bidding_igor = Bidding(igor, 100.0)
        bidding_amanda = Bidding(amanda, 150.0)

        auction = Auction('Celular')

        auction.biddings.append(bidding_igor)
        auction.biddings.append(bidding_amanda)

        evaluator = Evaluator()
        evaluator.evaluate(auction)

        lowest_expected_value = 100.0
        highest_expected_value = 150.0

        self.assertEqual(lowest_expected_value, evaluator.lowest_bidding)
        self.assertEqual(highest_expected_value, evaluator.highest_bidding)