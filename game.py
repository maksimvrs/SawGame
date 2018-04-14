import os, pygame

from settings import Settings
from objects.player import Player
from pygame import *

WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 640  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#004400"
bg = Surface((WIN_WIDTH, WIN_HEIGHT))
images = pygame.image.load(os.path.abspath('images/bg2.jpg'))

class Game():
	def __init__(self):
		self.player = Player(WIN_WIDTH / 2, 360)
		# pygame.init()  # Инициация PyGame, обязательная строчка
		# screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
		# будем использовать как фон
		bg.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом
		self.left = self.right = self.up = self.down = False

	def loop(self, screen):
		clock = pygame.time.Clock()
		scroll = 0

		while True:
			bg.blit(images, (0 + scroll, 0))
			screen.blit(bg, (0, 0))
			if (self.player.rect.x < 0 and scroll < 0):
				scroll += 2

			if (self.player.rect.x > 651 and scroll > -480):
				scroll -= 2

			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					return



				if e.type == KEYDOWN and e.key == K_LEFT:
					self.left = True
					self.player.rect.x += 2;
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


			self.player.update(self.left, self.right, self.up, self.down)
			self.player.draw(screen)
			pygame.display.update()

	def quit(self):
		pass