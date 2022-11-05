from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        arr = nums + nums
        stack = []
        res = [-1] * len(nums)
        for i in range(len(arr)-1, -1, -1):
            while stack and arr[i] >= stack[-1]:
                stack.pop()
            res[i%len(nums)] = stack[-1] if stack else -1
            stack.append(arr[i])
        return res 

s = Solution()
print(s.nextGreaterElements([1,2,1]))