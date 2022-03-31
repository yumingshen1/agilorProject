# -*- coding: utf-8 -*-
# @Time: 2022/3/22 17:00
# @Author: shenyuming

'''
    获得driver的对象方法和属性    tag标签，不太实用，一般不用，对head查找不友好
'''

from selenium import webdriver
from pathlib import Path
from time import sleep
import os
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
path = str(Path('one_html.html').resolve())
driver.get(path)
ele = driver.find_element(by=By.TAG_NAME, value='p')
ele2 = driver.find_element(by=By.TAG_NAME,value='title')

##获得元素后不知道有什么方法，可以用此方法
for _ in dir(ele):
    if _[0] != '_':
        print(_)
print(ele.text)

print('p标签的文本:',ele.text)
print('title标签的文本：',ele2.get_attribute('textContent'))

sleep(2)
driver.quit()






