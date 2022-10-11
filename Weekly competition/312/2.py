from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        p1, p2 = 0, 0
        n = len(nums)
        res = nums[0]
        max_res = 0
        max_len = 0
        while p1 < n and p2 < n:
            res &= nums[p2]
            p2 += 1
            if res < max_res:
                l = p2 - p1 - 1
                if l > max_len:
                    max_len = l
                p1 += 1
                p2 = p1
                res = nums[p1]
            elif res > max_res:
                max_res = res
        return max_len

s = Solution()
print(s.longestSubarray([1,2,3,3,2]))