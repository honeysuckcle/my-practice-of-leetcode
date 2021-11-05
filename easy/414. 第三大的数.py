"""
Date: 2021/10/6
三种方法
"""
from typing import List

# 方法一 排序
def thirdMax_fun1(nums: List[int]) -> int:
        nums.sort(reverse = True)
        diff = 1
        pre = nums[0]
        for x in nums:
            if x != pre:
                diff += 1
            if diff == 3:
                return x
            pre = x
        return nums[0]

# 方法二 有序集合
from sortedcontainers import SortedList

def thirdMax_fun2(nums: List[int]) -> int:
    s = SortedList()
    for num in nums:
        if num not in nums:
            s.add(num)
            if len(s) > 3:
                s.pop(0)
    if len(s) == 3:
        return s[0]
    else:
        return s[-1] 
