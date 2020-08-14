import unittest

from src.card import Card
from src.card_game import CardGame

class CardGameTest(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("Hearts", 1)
        self.card2 = Card("Diamonds", 9)
        self.card_game1 = CardGame(self.card1, self.card2)


    def test_if_card_is_ace_true(self):
        result = self.card_game1.check_for_ace(self.card1)
        self.assertEqual(True, result)

    def test_if_card_is_highest_card(self):
        result = self.card_game1.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2, result)

    def test_cards_total(self):
        cards = [self.card1, self.card2]
        result = self.card_game1.cards_total(cards)
        self.assertEqual("You have a total of 10", result)