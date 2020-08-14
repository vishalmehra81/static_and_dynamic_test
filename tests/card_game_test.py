import unittest

from src.card import Card
from src.card_game import CardGame

class CardGameTest(unittest.TestCase):

    def test_checkforAce(self):
        result = checkforAce(1)
        self.assertEqual(True, result)

    def test_highest_card(self):
        result = highest_card(1,2)
        self.assertEqual(2, result)

    def test_cards_total(self):
        result = cards_total(3)
        self.assertEqual("You have a total of 6", result)