# -*- coding: utf-8 -*-
# @Time: 2022/4/1 11:03
# @Author: shenyuming

'''
    xpath 函数法
    starts-with （@属性,属性开头的值）
    contains (@属性,属性包含的值)
    ends-with (@属性,属性结尾的值)
    text()='文本'  #替代link_text
    contains(text(),文本包含的值) #替代partial_link_text
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
from time import sleep

with webdriver.Chrome() as driver:
    path = str(Path('one_html.html').resolve())
    driver.get(path)
    sleep(1)
    # driver.find_element(by=By.XPATH, value="//*[starts-with(@value,'2')]").click()      #所有标签下值以2开头的value属性的元素
    #
    # driver.find_element(by=By.XPATH,value="//input[starts-with(@class,'b')]").send_keys('123')  #所有input下值以b开头的class属性的元素
    #
    # driver.find_element(by=By.XPATH,value="//input[contains(@name,'e')]").send_keys('大爷')  #所有input下值以e结尾的name属性的元素
    #
    # driver.find_element(by=By.XPATH,value="//a[text()='百度一下，你就知道']").click() #所有的a标签下，文本值=百度一下，你就知道 的元素
    #
    # driver.find_element(by=By.XPATH,value="//a[contains(text(),'必')]").click()  #所有的a标签下 文本包含 必的元素
    #
    # driver.find_element(by=By.XPATH,value="//div/input[last()]").click()        #所有的div下，最后一个input标签
    #
    # driver.find_element(by=By.XPATH,value="/html/body/div[1]/input[last()-1]").send_keys('name')  #所有的 /body/div[1]下的倒数第二个input标签

    text = driver.find_element(by=By.XPATH,value="//div/ul/li[position()<3]").text      ## //div/ul/目录下 前两个li
    print(text)
    sleep(2)