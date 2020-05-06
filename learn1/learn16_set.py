#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from learn1.learn17_file import my_util

edus = ['不限', '大专', '本科', '硕士']

try :
    a = edus.index('www')

except ValueError:
    print(233)
    a = 0

print(a)