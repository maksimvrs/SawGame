#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
from objects.item import Item
from communicate.communicate import Communicate

class Jail(Item):
    name = "Заключенный"

    communicate = Communicate(["1", "2", "3"])

    def action(self):
        self.currentText = self.communicate.next()
