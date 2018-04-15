#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
from objects.item import Item
from communicate.communicate import Communicate

class Books(Item):
    name = "Книги"

    communicate = Communicate(["1", "2", "3"])

    def action(self):
        self.currentText = self.communicate.next()
