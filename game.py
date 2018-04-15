import os, pygame

from settings import Settings
from objects.player import Player
from objects.item import Item
from objects.chest import Chest
from objects.picture import Picture
from objects.jail import Jail
from objects.books import Books
from objects.table import Table
from communicate.communicate import Communicate
from dialog import Dialog
# from text_window import TextObject
from pygame import *



WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 640  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#004400"
bg = Surface((WIN_WIDTH, WIN_HEIGHT))
images = pygame.image.load(os.path.abspath('images/bg4.jpg'))

class Game():
	def __init__(self):
		self.scroll = 0

		self.player = Player(WIN_WIDTH / 2, 360)

		self.items = [Chest(WIN_WIDTH / 2 + 540, 310, 'images/case.png', "Сейф 1", 320 // 4, 240 // 3),
					  Picture(WIN_WIDTH / 2 - 150, 240, 'images/picture.png', "Картина", 320 // 4, 240 // 3),
					  Books(WIN_WIDTH / 2 + 200, 300, 'images/books.png', "Книги",320 // 2, 240 // 2),
					  Jail(WIN_WIDTH / 2 + 750, 269, 'images/jail.png', "Заключенный", 320, 240),
					  Table(WIN_WIDTH / 2 - 300, 300, 'images/table.png', "Стол", 320 // 2, 240 // 2)]

		self.dialog = Dialog("- Добро пожаловать в мир твоих самых страшных кошмаров, жалкий офисный червяк.")

		self.left = self.right = self.up = self.down = False


	def loop(self, screen):
		clock = pygame.time.Clock()

		communicate = Communicate(["- Что, где я ?", "- Добро пожаловать в мир твоих самых страшных кошмаров, жалкий офисный червяк", "- Я ничего не понимаю, что происходит, я просто пошел за кофе, а потом… Ничего не помню", "- Вся твоя жизнь - самый скучный симулятор, но сейчас у тебя появился шанс хотя бы умереть интересно ",
								   "- Что, нет, выпустите меня", "- Единственный, кто может выпустить тебя - ты сам, ты всю жизнь думал за других, решал за других , пришло время отвечать за себя", "- Но кто это, почему, за что?", "- Ты знаешь…", "- *Пришло время выбираться, кроме себя, тебе не на кого надеяться, поэтому сделай что-нибудь, чтобы выжить*"])

		while True:
			bg.blit(images, (0 + self.scroll, 0))
			for i in self.items:
				i.update()
				i.draw(bg, self.scroll)
			screen.blit(bg, (0, 0))
			if (self.player.rect.x < 0 and self.scroll < 0):
				self.scroll += 2

			if (self.player.rect.x > 651 and self.scroll > -480):
				self.scroll -= 2

			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					return

				if e.type == KEYDOWN and e.key == K_LEFT:
					self.left = True
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

				if e.type == KEYDOWN and e.key == K_SPACE:
				    self.down = True
				if e.type == KEYUP and e.key == K_SPACE:
				    self.down = False

				# if e.type == KEYUP and e.key == K_DOWN:
				#     up = False


			self.player.update(self.left, self.right, self.down, self.items, self.scroll, self.dialog)
			if (self.down == True):
				communicate.currentText = communicate.next()
			if (len(communicate.data) > 0):
				self.dialog.setText(communicate.data[0])
			self.player.draw(screen)
			self.dialog.draw(screen)

			self.down = False

			pygame.display.update()

	def quit(self):
		pass