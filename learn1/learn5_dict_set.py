#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# dict 的用法 学生姓名-成绩 dict 字典
student_dict = {'sss1': 71, 'sss2': 12, 'sss3': 1, 'sss4': 100}

print(student_dict)
print(student_dict['sss1'])

student_dict['sss1'] = 100
print(student_dict['sss1'])

# 是否在字典内，防止报错
print('sss5' in student_dict)

# 自定义返回 -1
print(student_dict.get('sss999', -1))

# 删除sss1

student_dict.pop('sss1')
print(student_dict)

# 提一下set

score_set = set([1, 2, 3, 4, 5, 5, 6, 7])
score_set.add(8)
score_set.remove(1)

print(score_set)
