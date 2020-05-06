#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from selenium import webdriver

# 创建的新实例驱动
options = webdriver.FirefoxOptions()
#火狐无头模式
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Firefox()
driver.get(
    "https://www.cnblogs.com/pick/")

# 得到网页 html, 还能截图
html = driver.page_source  # get html
print(html)
driver.close()
