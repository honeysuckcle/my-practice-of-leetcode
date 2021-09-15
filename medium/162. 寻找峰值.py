"""
Date: 2021/9/15
算法：二分的迭代爬坡
类似梯度下降法则
时间复杂度：O(logn)
执行用时：28 ms, 在所有 Python3 提交中击败了89.55%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了80.01%的用户
"""
from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = int((left + right)/2)
            if mid == 0:
                if nums[0] > nums[1]:
                    return 0
                else:
                    left = 1

            if mid == (len(nums) - 1) :
                if nums[mid] > nums[mid - 1]:
                    return mid
                else:
                    right = mid - 1

            if nums[mid] > nums[mid - 1]:
                if nums[mid] > nums[mid + 1]:
                    return mid
                else:
                    left = mid + 1
            else:
                right = mid - 1
        return left