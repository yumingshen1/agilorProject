# -*- coding: utf-8 -*-
# @Time: 2022/3/31 15:08
# @Author: shenyuming

'''
    xpath路径法
    绝对路径不常用，元素改变时不适用
    相对路径
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep

with webdriver.Chrome() as driver:
    file_path = os.path.dirname(__file__)
    path = os.path.join(file_path,'two_html.html')
    driver.get(path)
    sleep(1)
    content = driver.find_element(by=By.XPATH,value='/html/body/div/div[1]/p').text     ## 绝对路径
    print(content)
    driver.find_element(by=By.XPATH,value='//body/div/div[2]/input').click()    #相对路径
    sleep(2)
