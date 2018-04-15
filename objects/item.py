#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *

class Item(sprite.Sprite):

    images = []

    def __init__(self, x, y, image_path, name):
        sprite.Sprite.__init__(self)

        self.name = name
        self.currentText = "Нажмите для взаимодействия с " + name

        self.startX = x
        self.startY = y

        self.index = 0

        self.images.append(transform.scale(image.load(image_path), (320 // 4, 240 // 3)))

        self.image = self.images[self.index]

        self.rect = self.image.get_rect()
        self.rect.center = (self.startX, self.startY)

    def action(self):
        pass

    def update(self):
        pass

    def draw(self, screen, scroll):
        screen.blit(self.image, (self.rect.x + scroll, self.rect.y))