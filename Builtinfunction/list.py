# -*- coding: utf-8 -*-
# @Time: 2022/3/11 14:59
# @Author: shenyuming

'''
列表都可以进行的操作包括索引，切片，加，乘，检查成员。
列表是最常用的 Python 数据类型，它可以作为一个方括号内的逗号分隔值出现。

列表的数据项不需要具有相同的类型

创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。
'''
from builtins import list

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
    给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
    二分法
'''

class Solution5:
    def searchInsert(self, nums: List[int], target: int) -> int:
        h = len(nums) -1
        print('list下标长度',h)
        l = 0
        if target>nums[h]:  #判断target是否大于列表的最后一个数
            return h+1
        elif target<nums[0]: #判断target是否小于列表的第一个数
            return 0
        while l<=h:
            mid = l+(h-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                h = mid -1
            else:
                l = mid+1
        return l
nums = [1,2,3,5,6]
target = 5
Solution5().searchInsert(nums,target)




'''
 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字
'''
class Solution6:
    def plusOne(self,digits:List[int]) -> int:
        for index in range(len(digits)-1,-1, -1): #倒叙循环
            if digits[index] < 9:           #元素值小于9，直接+1赋值，返回
                digits[index] += 1
                return digits
            else:                       ## 元素值不小于9，重新复制为0
                digits[index] = 0
        else:
            return [1]+digits       ## 返回不小于9元素前加1


    def plusOne2(self,digits:List[int]) -> int:
        for i in range(len(digits)+1,1,-1):    #遍历每一个值
            if(digits[-1]>=9):  #如果列表最后一个元素大于等于9则赋值为1在加0返回
                digits[-1] = 1
                digits.append(0)
                return digits
            else:                   # 列表元素最后一个小于9，则+1 后退出循环
                digits[-1]+=1
                return digits
                break
        # else:
        #     if(digits[-1]>=9):       #元素大于等于9时，那么第一位为1后面加0
        #         digits[-1] = 1
        #         digits.append(0)
        #     return digits

list = [7,3,9]
print(Solution6().plusOne(list))
list2 = [5,6,3]
print(Solution6().plusOne2(list2))


'''
    给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
'''

class Solution7:
    def deleteDuplicates(self, head):
        if head is None:
            return None
        cur = head
        while cur.next != None:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
p = [1,1,2,2,5,5,7,9]
# print(Solution7().deleteDuplicates(p))



'''
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。

'''


