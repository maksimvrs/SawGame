import os
import pygame
from pygame import *

class Dialog(sprite.Sprite):
    isNull = True
    def __init__(self, text = ""):
        self.setRightEnemy('images/enemy2.jpg')
        self.setLeftEnemy('images/enemy1.png')

        self.font = font.SysFont("comicsansms", 14)
        self.setText(text)

    def setText(self, text):
        if text:
            self.isNull = False
        self.text = self.font.render(text, True, (0, 128, 0))

    def clear(self):
        self.isNull = True
        self.text = ""

    def setRightEnemy(self, imageFile):
        self.enemyRight = image.load(os.path.abspath(imageFile))
        self.enemyRight = transform.scale(self.enemyRight, (320, 240))

    def setLeftEnemy(self, imageFile):
        self.enemyLeft = image.load(os.path.abspath(imageFile))
        self.enemyLeft = transform.scale(self.enemyLeft, (320, 240))

    def draw(self, screen):
        screen.blit(self.enemyRight, (600, -50))
        screen.blit(self.enemyLeft, (-50, -50))

        if not self.isNull:
            pf = Surface((475, 80))
            pf.fill((0, 0, 0))
            screen.blit(pf, (160, 5))

            screen.blit(self.text, (165, 15))