# -*- coding: utf-8 -*-
# @Time: 2022/3/31 14:09
# @Author: shenyuming
'''
    name属性定位
'''

from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    file_path = os.path.dirname(__file__)
    path = os.path.join(file_path,'one_html.html')
    driver.get(path)
    sleep(1)
    driver.find_element(by=By.NAME,value='name').send_keys('用户名')
    driver.find_element(by=By.NAME,value='pa').send_keys('passowrd')
    sleep(1)