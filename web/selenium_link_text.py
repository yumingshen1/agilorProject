# -*- coding: utf-8 -*-
# @Time: 2022/3/31 14:45
# @Author: shenyuming

'''
    link_text 两种定位，只适用于A标签
    link_text 完全匹配
    parti_link_text 模糊匹配
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
from time import sleep

with webdriver.Chrome() as driver:
    path = str(Path('one_html.html').resolve())
    driver.get(path)
    sleep(1)
    # driver.find_element(by=By.LINK_TEXT,value='有求必应').click()   #link_text
    driver.find_element(by=By.PARTIAL_LINK_TEXT,value='一下').click()
    sleep(2)