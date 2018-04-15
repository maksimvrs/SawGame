#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
from objects.item import Item
from communicate.communicate import Communicate

class Chest(Item):
    name = "Сейф"

    communicate = Communicate(["Почему этот сундук открыт?", "Замок сломан...", "Это странно..."])

    def action(self):
        self.image = transform.scale(image.load('images/casewithkey.png'), (320 // 4, 240 // 3))
        self.image = transform.scale(image.load('images/emptycase.png'), (320 // 4, 240 // 3))
        self.currentText = self.communicate.next()
