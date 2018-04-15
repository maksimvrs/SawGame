#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
from objects.item import Item
from communicate.communicate import Communicate

class Jail(Item):
    name = "Заключенный"

    communicate = Communicate(["Вы видите человека в клетке, в ваших силах спасти его, ценой своей жизни или нет", "подумайте", "ваши предыдущие решения влияют на любое ваше действие, как знать, кто за этой решеткой, ваш друг или злостный убийца? Решение за вами…"])

    def action(self):
        self.currentText = self.communicate.next()
