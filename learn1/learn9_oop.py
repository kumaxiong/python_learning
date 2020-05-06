#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Animal(object):
    def run(self):
        print('Animal is running')


class Dog(Animal):
    def run(self):
        print('Dog is running')


class Cat(Animal):
    def run(self):
        print('Cat is running')


def run_twice(animal):
    animal.run()
    animal.run()


# 多态：自动调用子类的run方法
run_twice(Animal())
run_twice(Dog())


