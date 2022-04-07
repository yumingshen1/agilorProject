# -*- coding: utf-8 -*-
# @Time: 2022/4/1 14:57
# @Author: shenyuming
'''
    xpath 轴定位，向上推
ancestor	选取当前节点的所有先辈（父、祖父等）。
ancestor-or-self	选取当前节点的所有先辈（父、祖父等）以及当前节点本身。
attribute	选取当前节点的所有属性。
child	选取当前节点的所有子元素。
descendant	选取当前节点的所有后代元素（子、孙等）。
descendant-or-self	选取当前节点的所有后代元素（子、孙等）以及当前节点本身。
following	选取文档中当前节点的结束标签之后的所有节点。
namespace	选取当前节点的所有命名空间节点。
parent	选取当前节点的父节点。
preceding	选取文档中当前节点的开始标签之前的所有节点。
preceding-sibling	选取当前节点之前的所有同级节点。
self	选取当前节点。
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

with webdriver.Chrome() as driver:
    file_path = os.path.dirname(__file__)
    path = os.path.join(file_path,'one_html.html')
    driver.get(path)
    sleep(1)
    text1 = driver.find_element(by=By.XPATH,value="//input/ancestor::div").text      #轴定位， 反着推，往上找 //input/的div先辈

    text2 = driver.find_element(by=By.XPATH,value="//div[5]/select[child::text()]").text     #查找 //div[5]/select下的所有子孙的文本

    print(text1,text2)
    sleep(1)