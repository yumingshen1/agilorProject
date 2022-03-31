# -*- coding: utf-8 -*-
# @Time: 2022/3/18 10:22
# @Author: shenyuming

from selenium import webdriver
# selenium物理地址：C:\Users\dell\AppData\Local\Programs\Python\Python310\Lib\site-packages\selenium
# 导入webdriver等同于：from .chrome.webdriver import WebDriver as Chrome
import time,os

driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# time.sleep(3)
# driver.close()

'''
    浏览器启动方式
'''

'''
    通过os模块 工程路径打开本地文件
'''
print(__file__)                 #当前文件路径
html = (os.path.dirname(__file__)) # 当前文件所在路径 ， abspath 当前文件所在位置
html_path = os.path.join(html,'one_html.html')
# driver.get(html_path)

'''
    绝对路径打开本地文件
'''
# driver.get(r'E:\sym\agilorProject\web\one_html.html')


'''
    利用pathlib库打开本地文件
'''
from pathlib import Path
# path = str(Path('one_html.html').resolve())
# driver.get(path)


'''
    优雅的打开网页，自动关闭  ，service_args=['--verbose'],service_log_path='selenium.log' ===> 生成报告+位置
'''
with webdriver.Chrome(service_args=['--verbose'],service_log_path='selenium.log') as driver:
    driver.get('https://cn.bing.com')
    driver.maximize_window()
    time.sleep(3)
    driver.find_element('id','sb_form_q').send_keys('Agilor')
    driver.find_element('id','search_icon').click()
    time.sleep(5)


## 找除了 _ 开头的全部方法
# test_flage = 2
# if test_flage ==1:
#     for _ in dir(driver):
#         if _[0] != '_':
#             print(_)
#
# ## 找find开头的方法
# if test_flage ==2:
#     for _ in dir(driver):
#         if _[:4] == 'find':
#             print(_)