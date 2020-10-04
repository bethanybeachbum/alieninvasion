# button.py

import pygame.font

class Button:

	def _init__(self, ai_game, msg):
		"""Initialize button attributes. """
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		# Set the dimensions and proporties of the button.
		self.width, self.height = 200, 50
		self.button_color = (0, 255, 0 )
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		# Build the button's rect object and coenter it.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		# Build the button's rect object and center it.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		# The button message needs to be prepped only once.
		self._prep_msg(msg)

	def _prep_msg(self, msg):
		"""Turn msg into a rendered image and centertext on the button. """
		# The call to font.render() turns text stored in "msg" to an image
		# we store the image in a variable we call self.msg_image
		# The boolean value turns antialiasing on or off
		# 3rd and 4th parameters are font color and background color
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		# Draw blank button and then draw message.
		# screen.fill() and screen.blit() are built in functions to Pygame
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
		


