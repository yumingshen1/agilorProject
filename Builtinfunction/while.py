# -*- coding: utf-8 -*-
# @Time: 2022/3/11 10:21
# @Author: shenyuming

'''
    while 判断条件(condition)：
    执行语句(statements)……
'''

a = 1
while a<10:
    print(a)
    a+=2


### while 实现1到100之间的和
n = 100
sum = 0
count = 1
while count <=n:
    sum = sum+count
    count+=1
print('1到100之间的和为%d:'%sum)


## while无线循环数据
# var =1
# while var ==1:
#     try:
#         num = int(input("请输入一个数字："))
#         print("您输入的是%d："%num)
#     except:
#         print("输入了非法字符：如特殊符号，空格，字母等")

import re
var = 1
while var == 1:
    try:
        num = (input("请输入一个数字："))
        my_re = re.compile(r'[A-Za-z]',re.S)
        res = re.findall(my_re,num)
        if len(res):
            print('有字符串,请重新输入')
        else:
            if num == "":
                print('您未输入字符')
            elif num == " ":
                print("您输入的是空格")
            else:
                print("您输入的是%s："%num)
    except:
        print("可能是特殊字符！@#￥%……&*（）《》？：“{}|等！！")



### 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
class Solution:
    def isValid(self,s:str)->bool:
        if len(s) < 2 or len(s)%2 != 0:     ##判断是否为奇数或者小于2
            if s == '':
                print('True---')
            else:
                print('False---')
        count = 0
        length = len(s)
        while (count < length/2):           ## count小于字符串的一半 就将每个括号替换
            s = s.replace("{}","").replace("[]","").replace("()","")
            count+=1
        if len(s) > 0:
            print('False...')
        else:
            print('True...')

ss = " '('，')'，'{'，'}'，'['，']' "
Solution().isValid(ss)