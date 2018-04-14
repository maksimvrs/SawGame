import os, pygame

from settings import Settings
from objects.player import Player
from objects.item import Item
# from text_window import TextObject
from pygame import *



WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 640  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#004400"
bg = Surface((WIN_WIDTH, WIN_HEIGHT))
images = pygame.image.load(os.path.abspath('images/bg2.jpg'))
enemy = pygame.image.load(os.path.abspath('images/enemy.jpg'))
enemy = pygame.transform.scale(enemy, (320, 240))

class Game():
	def __init__(self):
		self.scroll = 0

		self.player = Player(WIN_WIDTH / 2, 360)

		self.items = [Item(WIN_WIDTH / 2, 310)]

		self.left = self.right = self.up = self.down = False


	def loop(self, screen):
		clock = pygame.time.Clock()

		while True:
			bg.blit(images, (0 + self.scroll, 0))
			for i in self.items:
				i.update()
				i.draw(bg, self.scroll)
			screen.blit(bg, (0, 0))
			screen.blit(enemy, (600, -50))
			if (self.player.rect.x < 0 and self.scroll < 0):
				self.scroll += 2

			if (self.player.rect.x > 651 and self.scroll > -480):
				self.scroll -= 2

			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					return



				if e.type == KEYDOWN and e.key == K_LEFT:
					self.left = True
					self.player.rect.x += 2
				if e.type == KEYDOWN and e.key == K_RIGHT:
					self.right = True

				# if e.type == KEYDOWN and e.key == K_UP:
				#     down = True
				# if e.type == KEYDOWN and e.key == K_DOWN:
				#     up = True

				if e.type == KEYUP and e.key == K_LEFT:
					self.left = False
				if e.type == KEYUP and e.key == K_RIGHT:
					self.right = False

				# if e.type == KEYUP and e.key == K_UP:
				#     down = False
				# if e.type == KEYUP and e.key == K_DOWN:
				#     up = False


			self.player.update(self.left, self.right, self.items, self.scroll)
			self.player.draw(screen)
			# self.TextObject.drow()

			pygame.display.update()

	def quit(self):
		pass