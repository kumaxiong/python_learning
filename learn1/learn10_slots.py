#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    # 定义变量，只能有这些
    __slots__ = ('name', 'score', '__id')

    # 类似构造函数
    def __init__(self, name, score, id=1):
        self.name = name
        self.score = score
        # 私有变量不能从外部访问
        self.__id = id


ss1 = Student('ss1', 100)
