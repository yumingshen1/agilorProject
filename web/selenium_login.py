# -*- coding: utf-8 -*-
# @Time: 2022/3/31 15:01
# @Author: shenyuming

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

with webdriver.Chrome() as driver:
    driver.get('http://120.55.190.222:38090/#/login')
    sleep(2)
    driver.find_element(by=By.NAME,value='username').send_keys('鸿星尔克286')
    driver.find_element(by=By.NAME,value='password').send_keys('123456')
    driver.find_element(by=By.CLASS_NAME,value='el-button').click()
    sleep(2)

