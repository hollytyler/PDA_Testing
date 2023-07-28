import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card_game = CardGame()
        self.card1 = Card("spade", 1)
        self.card2 = Card("diamond", 5)
        self.card3 = Card("hearts", 6)
        self.cards = [self.card1, self.card2, self.card3]

    def test_check_for_ace(self):
        actual = self.card_game.check_for_ace(self.card1)
        expected = True
        self.assertEqual(expected, actual)

    def test_highest_card(self):
        actual = self.card_game.highest_card(self.card1, self.card2)
        expected = self.card2
        self.assertEqual(expected, actual)

    def test_cards_total(self):
        actual = self.card_game.cards_total(self.cards)
        expected ="You have a total of 12"
        self.assertEqual(expected, actual)