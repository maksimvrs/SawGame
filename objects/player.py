#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *

MOVE_SPEED = 2

WIDTH = 22
HEIGHT = 32
COLOR = "#888888"


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.yvel = 0
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект

    def update(self, left, right, up, down):
        if left:
            self.xvel = -MOVE_SPEED  # Лево = x- n

        if right:
            self.xvel = MOVE_SPEED  # Право = x + n

        if up:
            self.yvel = MOVE_SPEED * 0.75

        if down:
            self.yvel = -MOVE_SPEED * 0.75

        if not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0

        if not (up or down):
            self.yvel = 0

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.rect.y += self.yvel

    def draw(self, screen):  # Выводим себя на экран
        screen.blit(self.image, (self.rect.x, self.rect.y))