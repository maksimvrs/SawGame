#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
OPENED_CHEST = 'img.png'
CLOSED_CHEST = 'img.png'
WIDTH = 25
HEIGHT = 25
COLOR = "#888888"
IS_OPEN = False

class Chest(sprite.Sprite):
    IS_OPEN = False
    OPENED_CHEST = 'img.png'
    CLOSED_CHEST = 'img.png'
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.startX = x  # позиция сундука
        self.startY = y
        self.opened_image = Surface((WIDTH, HEIGHT))
        self.closed_image = Surface((WIDTH, HEIGHT))
        self.opened_image.fill(Color(COLOR))
        self.closed_image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект

    def update(self, keyPressed):
       if keyPressed:
           self.IS_OPEN = True
        pass

    def draw(self, screen):  # Выводим себя на экран
        if(IS_OPEN)
            screen.blit(self.opened_image, (self.rect.x, self.rect.y))
        else:
            screen.blit(self.closed_image, (self.rect.x, self.rect.y))
