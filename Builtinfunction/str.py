# -*- coding: utf-8 -*-
# @Time: 2022/3/23 15:51
# @Author: shenyuming
'''
    给你两个字符haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回 -1 。
'''
from builtins import str


class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        len1=len(needle)
        print('needle长度',len1)
        if len1==0:
            return 0
        for i in range(len(haystack)):
            if haystack[i:i+len1]==needle:
                print(i)
        return -1

s1 = 'bfmllopk'
s2= 'll'
# Solution1().strStr(s1,s2)


'''
    给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。
单词 是指仅由字母组成、不包含任何空格字符的最大子
'''

class Solution2:
    def lengthOfLastWord(self,s: str) -> int:
        ##先将S前后空格去掉，进行切片处理,返回一个list
        temp_list = s.strip().split(" ")
        print('切割后的list:',temp_list)
        for i in temp_list[::-1]: #从最后一个开始循环
            print('最后一个值：',i)
            if i != " ":
                print('最后一个单词的长度：',len(i))
                break
            else:
                continue
str = "   fly me   to   the moon  "
Solution2().lengthOfLastWord(str)