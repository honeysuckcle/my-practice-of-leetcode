from inspect import stack
from tkinter import N
from typing import List
def the_next_greater():
    nums = [2,4,0,9,6]
    stack = []
    res = [-1 for _ in range(len(nums))]
    for i in range(len(nums)-1, -1, -1):
        # desent
        while len(stack) != 0 and nums[i] > stack[-1]:
            stack.pop()
        res[i] = -1 if len(stack) == 0 else stack[-1]
        stack.append(nums[i])
    print(res)
    
class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n 
        s, t = [], []
        for i in range(n):
            while t and nums[i] > nums[t[-1]]:
                res[t[-1]] = nums[i]
                t.pop()
            j = len(s) -1
            while j>=0 and nums[i] > nums[s[j]]:
                j -= 1
            t += s[j+1:]
            del s[j+1:]
            s.append(i)
        return res


s = Solution()
print(s.secondGreaterElement([2,4,0,9,6]))
