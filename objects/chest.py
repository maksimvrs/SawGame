#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import time
from objects.item import Item

class Chest(Item):

    def action(self):
        self.image = transform.scale(image.load('images/3.png'), (320 // 4, 240 // 3))
        #time.sleep(5.5)