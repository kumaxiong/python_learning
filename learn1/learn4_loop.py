#!/usr/bin/env python3
# -*- coding: utf-8 -*-

student_list = ['sss1', 'sss2', 'sss3', 'sss4']
print(student_list)

# for 循环的使用，遍历
for student in student_list:
    print(student)

num_list = list(range(1, 101))
print(num_list)
sum = 0
for num in num_list:
    sum += num
    if num == 20:
        break

print(sum)


# while 循环
sum = 0
n = 1
while n <= 100:
    sum += n
    n += 1

print(sum)