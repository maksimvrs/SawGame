#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
from objects.item import Item
from communicate.communicate import Communicate

class Table(Item):
    name = "Стол"

    communicate = Communicate(["Этот стол в КРОВИ!!!", "ЭТО КРОВЬ!!!", "КУДА Я ПОПАЛ???"])

    def action(self):
        self.currentText = self.communicate.next()
