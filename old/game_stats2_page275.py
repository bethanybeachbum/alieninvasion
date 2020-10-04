# game_stats.py

class GameStats:
	""" Track statistics for Alien Invasion. """

	def __init__(self, ai_game):
		"""Initiate statistics"""
		self.settings = ai_game.settings
		self.reset_stats()

	def reset_stats(self):
		""" Initiate statistics that can chagne during the game. """
		self.ships_left = self.settings.ship_limit
