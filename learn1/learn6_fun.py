#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(abs(-1))
print(int('134123'))

# 变量指向函数名的引用

f = abs
print(f(-1137))


# 自己写一个绝对值函数
def my_abs(x):
    if x > 0:
        return x
    else:
        return -x


print(my_abs(-11))


# 默认参数
def my_add(x, y=1):
    return x + y


print(my_add(1, y=2))

# 可变参数

num_list = list(range(1, 10))


def my_sum(*nums):
    sum = 0
    for n in nums:
        sum += n
    return sum


print('sum is = %d' % my_sum(1, 2, 3))
print(my_sum(*num_list))


# 关键字参数
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


person_dict = {'city': 'beijing', 'job': '无业'}
person('ss1', 12, **person_dict)
