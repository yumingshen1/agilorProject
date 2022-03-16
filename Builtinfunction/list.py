# -*- coding: utf-8 -*-
# @Time: 2022/3/11 14:59
# @Author: shenyuming

'''
列表都可以进行的操作包括索引，切片，加，乘，检查成员。
列表是最常用的 Python 数据类型，它可以作为一个方括号内的逗号分隔值出现。

列表的数据项不需要具有相同的类型

创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。
'''

l1 = [1,2,4]
l2 = [1,3,4]

class Soultion:
    def mergeTwoLists(self,list1,list2):
        l3 = list1+list2
        l3.sort()
        print(l3)

    def me2(self,list1,list2):
        list1.extend(list2)
        list1.sort()
        print(l1)

Soultion().mergeTwoLists(l1,l2)

Soultion().me2(l1,l2)


#### 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
class Solution2:
    def mergeTwoLists2(self, list1: list[list], list2: list[list]) -> list:
        prevhead = list(0)  # 标识开头
        prev = prevhead  #标识结尾

        # 遍历两链表，如有None则跳出循环
        while list1 and list2:
            if list1.val <= list2.val: # l1的节点值小，prev指针指向l1，l1节点右移
                prev.next = list1
                list1 = list1.next
            else: # l2的节点值小，prev指针指向l2，l2节点右移
                prev.next = list2
                list2 = list2.next
            prev = prev.next

        # prev的next指针指向非空链表
        prev.next = list1 if list1 is not None else list2
        return prevhead.next
# Solution2().mergeTwoLists2(l1,l2)

'''
### 删除有序数组中的重复项,原地修改删除， 注意：遍历时删除会报错，删除list后 长度会变短，但是循环次数没变
'''
lists = [00,11,22,3,4,5,644,66,66,1,1,3,3,8,8]
from typing import List
class Solution3:
## 反向遍历删除法，从数组尾部删除不影响其他元素
    def removeDuplicates2(self,nums:List[int]) -> int:
        if len(nums) <= 0:
            return 0
        for i in range(len(nums)-1,0,-1):
            if nums[i] == nums[i-1]:
                nums.pop(i)
        print(nums)
Solution3().removeDuplicates2(lists)

'''
    给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
'''
## 双指针
class Solution4:
    def removeElment(self,nums:List[int],val):
        left = 0        ## 定义一个数，用来标记长度
        for i in range(len(nums)):
            if nums[i] != val:
                # nums[left] = nums[i]
                left +=1
        print(left)

    # 给你一个数组 nums 和一个值 val，将不等于val的值写入新的数组，打印出来
    def removeElment2(self,nums:list,val):
        num = []
        for i in range(len(nums)):
            if nums[i] != val:
                num.append(nums[i])
        print(num)

n = [1,3,5,7,0]
v = 5
Solution4().removeElment(n,v)
Solution4().removeElment2(n,v)


'''
    给你两个字符haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回 -1 。
'''
class Solution5:
    def strStr(self, haystack: str, needle: str) -> int:
        len1=len(needle)
        if len1==0:
            return 0
        for i in range(len(haystack)):
            if haystack[i:i+len1]==needle:
                print(i)
        return -1

s1 = 'bfmllopk'
s2= 'll'
Solution5().strStr(s1,s2)