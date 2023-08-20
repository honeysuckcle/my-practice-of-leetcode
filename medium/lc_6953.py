from typing import List
class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        if len(nums) == 1 or (len(nums) == 2 and sum(nums) >= m):
            return True
        left, right, mid = False, False, False
        if sum(nums[1:]) >= m:
            left = self.canSplitArray(nums[1:], m)
        if left:
            return True
        if sum(nums[:-1]) >= m:
            right = self.canSplitArray(nums[:-1], m)
        if right:
            return right
        for i in range(2, len(nums)-1):
            mid = self.canSplitArray(nums[:i], m) and self.canSplitArray(nums[i:], m)
            if mid:
                return mid
        return False
    
s = Solution()
print(s.canSplitArray([1,2,1,1], 4))