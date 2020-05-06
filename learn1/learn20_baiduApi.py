#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '11241130'
API_KEY = 'G1NDPS1xKibg79NxzLfnnnIy'
SECRET_KEY = '6l8HQYLHKs7jjVvHTXt5Tk6YRg9vuBPL'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('233.jpg')

result = client.basicAccurate(image)
print(result)
# print(url)