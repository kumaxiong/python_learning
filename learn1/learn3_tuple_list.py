#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list 用法

student_list = ['sss1', 'sss2', 'sss3', 'sss4']
text = ''
for i in student_list:
    print(i)

print(text)
print(student_list)
# len() 函数显示长度

print(len(student_list),)


# 下标访问

print(student_list[1], )
print(student_list[-1], )

# 列表可变的， 追加，插入，弹出

# student_list.append('sss5')
student_list.insert(1, 'sss5')
student_list.pop(1)
print(student_list)


p = [1, 2, 3]
s = ['x', p, 'y']
print(p[1])
print(s[1][1])

# tuple 用法

# student_tuple = tuple(student_list)
student_tuple = ('sss1', p, 'sss3', 'sss4', 'sss5')

student_tuple[1][1] = 3

