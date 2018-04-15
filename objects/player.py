#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import math

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
        # self.image = Surface((WIDTH, HEIGHT))
        # self.image.fill(Color(COLOR))
        # self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект

        self.imagesLeft = []
        self.imagesRight = []
        self.imagesFront = []
        self.imagesRight.append(transform.scale(image.load('images/1.png'), (320 // 2, 240 // 2)))
        self.imagesRight.append(transform.scale(image.load('images/5.png'), (320 // 2, 240 // 2)))
        self.imagesLeft.append(transform.scale(image.load('images/3.png'), (320 // 2, 240 // 2)))
        self.imagesLeft.append(transform.scale(image.load('images/4.png'), (320 // 2, 240 // 2)))
        self.imagesFront.append(transform.scale(image.load('images/2.png'), (320 // 2, 240 // 2)))
        self.index = 0
        self.image = self.imagesFront[self.index]

        self.image = transform.scale(self.image, (320, 240))
        self.rect = self.image.get_rect()
        self.rect.center = (self.startX, self.startY)

    def update(self, left, right, down, items, scroll, dialog):

        for item in items:
            if abs(item.rect.x + scroll - self.rect.x) < 60:
                dialog.setText(item.currentText)
                if (down):
                    print(item.currentText)
                    print(item.name)
                    item.action()
                break
            else:
                dialog.clear()

        if left:
            if (self.rect.x > 0):
                self.xvel = -MOVE_SPEED  # Лево = x- n
            else:
                self.rect.right = 320
            self.index += 0.1
            if math.floor(self.index) >= len(self.imagesLeft):
                self.index = 0
            self.image = self.imagesLeft[math.floor(self.index)]

        if right:
            if (self.rect.x < 650):
                self.xvel = MOVE_SPEED  # Право = x + n
            else:
                self.rect.right = 970
            self.index += 0.1
            if math.floor(self.index) >= len(self.imagesRight):
                self.index = 0
            self.image = self.imagesRight[math.floor(self.index)]

        # if up:
        #     self.yvel = MOVE_SPEED * 0.75
        #
        #
        # if down:
        #     self.yvel = -MOVE_SPEED * 0.75

        if not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0
            self.image = self.imagesFront[0]

        # if not (up or down):
        #     self.yvel = 0


        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.rect.y += self.yvel

    def draw(self, screen):  # Выводим себя на экран
        screen.blit(self.image, (self.rect.x, self.rect.y))