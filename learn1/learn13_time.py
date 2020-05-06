#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import time


def getTime(s):
    time_list = re.split(r'\s+', s)
    # l0 日 l1 月 l2 年
    print(time_list)


def getMonth(s):
    Months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    return Months.index(s) + 1


s = '29 Nov 2018'
l = time.strptime(s, '%d %b %Y')

s = 'Published on 8th January 2018, 11:55:29 UTC'
# getTime(s)
print(s.find('Published on '))
l = time.strptime(s, 'Published on %dth %B %Y, %H:%M:%S %Z')



s = '31 Jul. 2017'
l = time.strptime(s, '%d %b. %Y')

s = 'February 8, 2018'
l = time.strptime(s, '%B %d, %Y')

s = '\r\n            March 08, 2016  \r\n    \r\n'
s1 = re.sub('[\r|\n]', '', s)
s1 = s1.strip()
print(s1)
l = time.strptime(s1, '%B %d, %Y')

s = 'Last updated: January 24, 2018'
l = time.strptime(s, 'Last updated: %B %d, %Y')
s = 'April 4, 2018'
l = time.strptime(s, '%B %d, %Y')

s = '2018-03-30T17:41:38+00:00'
l = time.strptime(s, '%Y-%m-%dT%H:%M:%S+00:00')

s = '2015-12-28T20:55:31+02:00'
l = time .strptime(s,'%Y-%m-%dT%H:%M:%S+02:00')
print(l)
