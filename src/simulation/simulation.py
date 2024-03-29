
import collections

from ..game import Deck, Game

def run_simulation(runner, runs: int, base_deck: Deck, maps):

	scores = collections.Counter[str]()

	for _ in range(runs):

		base_deck.shuffle()

		for pattern, pattern_map in maps.items():

			deck = iter(base_deck)

			pattern_map.fill_checkpoints(deck)

			autoroute = Game(pattern_map)

			scores[pattern] += runner.play(autoroute, deck)

	return scores
