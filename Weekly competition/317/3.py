from typing import List
class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        nums = [0] * 13
        res = 0
        count = 0
        while n > 0:
            b = n % 10
            nums[count] = b
            count += 1
            n = n // 10
        if sum(nums) <= target:
            return 0
        sit = 0
        while sum(nums) > target:
            res += pow(10, sit) * (10 - nums[sit])
            nums[sit] = 0
            nums[sit+1] += 1
            sit += 1
        return res

s = Solution()
s.makeIntegerBeautiful(999, 1)