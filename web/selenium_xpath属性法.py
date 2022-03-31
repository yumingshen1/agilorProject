# -*- coding: utf-8 -*-
# @Time: 2022/3/31 15:35
# @Author: shenyuming
'''
    xpath 属性法 ，需要配合xpath相对路径使用
    class 的值要写全部
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
from time import sleep

with webdriver.Chrome() as driver:
    path = str(Path('two_html.html').resolve())
    driver.get(path)
    sleep(1)
    driver.find_element(by=By.XPATH,value="//input[@class='ls_ssen vm']").click()
    sleep(1)