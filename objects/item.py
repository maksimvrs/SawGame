#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *

class Item(sprite.Sprite):

    images = []

    def __init__(self, x, y, image_path, name, width, height):
        sprite.Sprite.__init__(self)

        self.name = name
        self.currentText = "Нажмите для взаимодействия с " + name

        self.startX = x
        self.startY = y

        self.image = transform.scale(image.load(image_path), (width, height))

        self.rect = self.image.get_rect()
        self.rect.center = (self.startX, self.startY)

        self.size = (width, height)

    def action(self):
        pass

    def update(self):
        pass

    def draw(self, screen, scroll):
        screen.blit(self.image, (self.rect.x + scroll, self.rect.y))