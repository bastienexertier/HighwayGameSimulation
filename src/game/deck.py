
from random import shuffle

from ..model import Card, VALUE, COLOR

class Deck:

	def __init__(self, cards:list[Card]):
		self.cards = cards

	@classmethod
	def new_52_cards_deck(cls):
		return cls(
			[
				Card(value, color)
				for value in range(len(VALUE))
				for color in range(len(COLOR))
			]
		)

	def shuffle(self):
		shuffle(self.cards)
		return self

	def __iter__(self):
		return iter(self.cards)
