#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *

class Item(sprite.Sprite):

    images = []

    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.startX = x
        self.startY = y

        self.index = 0

        self.images.append(transform.scale(image.load('images/1.png'), (320 // 2, 240 // 2)))

        self.image = self.images[self.index]

        self.rect = self.image.get_rect()
        self.rect.center = (self.startX, self.startY)

    def action(self):
        pass

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))