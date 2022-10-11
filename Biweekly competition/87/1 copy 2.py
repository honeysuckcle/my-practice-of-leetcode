from typing import List
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [[0 for _ in range(n+1)] for _ in range(n)]
        for i in range(len(nums)):
            dp[i][1] = nums[i]
        res = [0] * len(nums)
        for i in range(len(nums)):
            maxr = 0
            for j in range(1, len(nums) - i):
                dp[i][j] = dp[i][j-1] | nums[i+j-1]
                if dp[i][j] > maxr:
                    res[i] = j
                    maxr = dp[i][j]
        return res
s = Solution()
print(s.smallestSubarrays([1,0,2,1,3]))
        