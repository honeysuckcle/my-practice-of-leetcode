from typing import List
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        p, q = 0, 0
        n = len(nums)
        while p < n and q < n:
            if nums[q] - nums[p] <= nums[p]:
                ans = max(ans, nums[p] ^ nums[q])
                q += 1
                if q == n:
                    p += 1
                    q = p
            else:
                p += 1
                q = p
        return ans

s = Solution()
print(s.maximumStrongPairXor([2,3,4]))