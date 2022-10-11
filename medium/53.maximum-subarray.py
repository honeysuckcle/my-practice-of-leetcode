from cmath import inf
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)  == 1:
            return nums[0]
        if len(nums) == 0:
            return -inf
        mid = int(len(nums) /2)
        p1, p2 = mid-1, mid+1
        res_l = 0
        max_l = 0
        while p1 >= 0:
            res_l += nums[p1]
            if res_l > max_l:
                max_l = res_l
            p1 -= 1
        res_r = 0
        max_r = 0
        while p2 < len(nums):
            res_r += nums[p2]
            if res_r > max_r:
                max_r = res_r
            p2 += 1
        return max(self.maxSubArray(nums[:mid]), self.maxSubArray(nums[mid+1:]), nums[mid]+max_l+max_r)

s = Solution()
print(s.maxSubArray([-2, -1]))