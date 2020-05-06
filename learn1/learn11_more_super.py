#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    pass


# 大类:
class Mammal(Animal):
    pass


# # 各种动物:
# class Dog(Mammal):
#     pass
#
#
# class Bat(Mammal):
#     pass


class Runnable(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):
        print('Flying...')


class Bat(Mammal, Flyable):
    pass


class Dog(Mammal, Runnable):
    pass
