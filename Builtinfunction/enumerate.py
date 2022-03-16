# -*- coding: utf-8 -*-
# @Time: 2022/3/10 17:15
# @Author: shenyuming

'''
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中

语法----> enumerate(sequence, [start=0])       返回 enumerate(枚举) 对象。

sequence -- 一个序列、迭代器或其他支持迭代对象。
start -- 下标起始位置。
'''

sears = ['Spring','Summer','Fail','Winter']
a = list(enumerate(sears))
print('返回枚举对象：',a)

b = list(enumerate(sears,start=1))
print('下标从1开始',b)

## for循环
for i,element in enumerate(sears,start=1):
    print('循环打印的下表对应的值：',i,element)



### 编写一个函数来查找字符串数组中的最长公共前缀。

class Solution:
    def longCommentPrefix(self,strs: list[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            b = sorted(strs,key=lambda x:len(x))   ## 用字符串长度排序,返回从短到长的字符串
            s = ''
            s1 = b[0]
            for i,v in enumerate(s1):   # 对字符串第一个值枚举，遍历每一个字符
                l = []
                for j in b[1:]:         # 从第二个字符串开始 遍历所有的字符
                    l.append(v==j[i])  # 将相等的值添加到list
                if all(l):
                    s += v
                else:
                    break
        return s
str1 = ['fterwwqddfs','ftsdadklka','ftasdas']
text = Solution().longCommentPrefix(str1)
print(text)