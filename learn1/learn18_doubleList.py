#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# # for循环两个列表的过程
# list1 = ['1', '1']
# list2 = ['A', 'B']
#
# for x in list1, list2:
#     reslut = x[:]
#     print(reslut)  # type=list

# for循环两个列表的过程
list1 = [1, 2, 3, 4]
list2 = [11, 22, 33, 44]

for (x, y) in zip(list1, list2):
    print(x, '  ', y)
