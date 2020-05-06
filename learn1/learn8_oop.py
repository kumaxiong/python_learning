#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    # 类似构造函数
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_message(self):
        print('name is %s, score is %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


ss1 = Student('ss1', 10)
ss1.hand = 4
ss1.print_message()
print(ss1.hand)
