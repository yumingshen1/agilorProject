# -*- coding: utf-8 -*-
# @Time: 2022/3/31 14:18
# @Author: shenyuming
'''
    class属性定位
    一个元素内有多个值，只写一个，例如 :class = 'ls_ssen vm' , 只取 ‘ls_ssen’ 或者 ‘vm’
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
from time import sleep
import os

with webdriver.Chrome() as driver:
    path = str(Path('one_html.html').resolve())
    driver.get(path)
    driver.find_element(by=By.CLASS_NAME,value='aa').send_keys('名字')
    driver.find_element(by=By.CLASS_NAME,value='cc').send_keys('pass')
    driver.find_element(by=By.CLASS_NAME,value='bb').send_keys('word')
    sleep(1)