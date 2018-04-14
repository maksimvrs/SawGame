#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import time
from objects.item import Item

class Chest(Item):

    def action(self):
        self.image = transform.scale(image.load('images/casewithkey.png'), (320 // 4, 240 // 3))
        self.image = transform.scale(image.load('images/emptycase.png'), (320 // 4, 240 // 3))