from typing import List
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        def max_d(num):
            return max(map(int, list(str(num))))
        ans = -1
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if max_d(nums[i]) == max_d(nums[j]):
                    ans = max(nums[i]+nums[j], ans)
        return ans
    
s = Solution()
print(s.maxSum([51,71,17,24,42]))