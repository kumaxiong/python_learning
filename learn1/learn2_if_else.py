#!/usr/bin/env python3
# -*- coding: utf-8 -*-

age = 18

if age == 18:
    print('age = %s' % age)
    # print('age =', age)

# if else 语

age = 17
if age == 18:
    print('age = %s' % age)
else:
    print('age != %s' % 18)

# if elif
age = 18
flag = 1
if age == 18 and flag == 1:
    print('age = %s flag = %s' % (age, flag))
elif age == 17 or age == 16:
    print('age = 17 or age = 16')
else:
    print('no match')
