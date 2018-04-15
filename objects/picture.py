#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import time
from objects.item import Item
from communicate.communicate import Communicate

class Picture(Item):
    name = "Картина"

    communicate = Communicate(["Девушка на этой картине поразительно похожа на мою бывшую, да, не самое приятное расставание, ведь я изменил ей с её лучшей подругой прямо у неё на дне рождения . Стоило  ли оно того?"])

    def action(self):
        self.currentText = self.communicate.next()