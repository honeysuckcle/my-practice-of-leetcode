from typing import List
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = +inf
        def is_increase(arr):
            for i in range(1, len(arr)):
                if arr[i-1] >= arr[i]:
                    return False
            return True
        def is_decrease(arr):
            for i in range(1, len(arr)):
                if arr[i-1] <= arr[i]:
                    return False
            return True
        n = len(nums)
        init_left = nums[:k]
        init_right = nums[k+1:2*k+1]
        left = is_increase(init_left)
        right = is_decrease(init_right)
        res = []
        if left == False and right == False:
            res.append(k)
        for i in range(k+1, n-k):
            if nums[i-1] >= nums[i-2] and nums[i+1] <= nums[i+2]:
                res.append(i)
            elif is_increase(nums[i-k:i]) == False and is_decrease(nums[i+1:i+k+1]) == False:
                res.append(i)
        return res

s = Solution()
print(s.goodIndices([440043,276285,336957], 1))