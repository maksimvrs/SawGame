#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
from objects.item import Item
from communicate.communicate import Communicate

class Books(Item):
    name = "Книги"

    communicate = Communicate(["Ого, в таком грязном месте, а книга выглядит, как новая. Что? «Шоколад» Джоанн Харрис, это же любимая книга моей мамы?!", "Да что, черт возьми, здесь происходит?! ЧТО ТЫ ХОЧЕШЬ МНЕ ЭТИМ СКАЗАТЬ??", "ДА, Я ПОСТУПИЛ УЖАСНО, ДА, Я НЕ ОБЩАЮСЬ С НЕЙ УЖЕ 10 ЛЕТ!", "Боже, за что я такс ней??"])

    def action(self):
        self.currentText = self.communicate.next()
