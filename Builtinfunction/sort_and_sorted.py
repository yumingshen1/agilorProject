# -*- coding: utf-8 -*-
# @Time: 2022/3/10 16:35
# @Author: shenyuming
import cmp
'''
sort 与 sorted 区别：

sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。

list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。

语法------>：  sorted(iterable, key=None, reverse=False)  
iterable -- 可迭代对象。
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）
'''

A  = [5,2,3,4,9,7,6]
A.sort()
print('sort没有返回值，直接操作原有list：',A)

a = [4,5,7,1,3,8,9,6,4,2]
b = sorted(a)
print(a)
print('返回新的list:',b)

## 按 key排序，key固定，a:a自定义，[1]用第几个值排序
l = [('a',3),('f',1),('s',9),('e',12),('b',6)]
new_l1 = sorted(l,key=lambda a:a[1],reverse=False)
print('通过key lambda排序:',new_l1)


### 奖牌排行
s = "德国 10 11 16\n意大利 10 10 20\n荷兰 10 12 14\n法国 10 12 11\n英国 22 21 22\n中国 38 32 18\n日本 27 14 17\n美国 39 41 33\n俄罗斯奥委会 20 28 23\n澳大利亚 17 7 22\n匈牙利 6 7 7\n加拿大 7 6 11\n古巴 7 3 5\n巴西 7 6 8\n新西兰 7 6 7"
stodata = s.split('\n',-1)
# 使用sorted
para = {}
for line in range(len(stodata)):
    # 每一行数据
    data = stodata[line].split(' ')
    print(data)
    # 组装数据结构para={'China': [], 'Russia': []}
    para[data[0]] = [int('-' + i) for i in data[1:]]
# 开始排序(x[1]代表奖牌数目, x[0]代表国家)
new_para = sorted(para.items(), key=lambda x: (x[1], x[0]))
print()

c=[]
##国家排名
for i in new_para:
     c.append((i[0]))
for j in range(15):
    print(f"{(j+1):>2d}  {c[j]}")