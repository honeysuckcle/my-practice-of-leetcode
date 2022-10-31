from cmath import inf
from collections import defaultdict
from typing import List
from math import inf
class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        budget = defaultdict(int)
        index = defaultdict(int)
        max_ = 0
        max_i = inf
        for i in range(len(nums)):
            budget[nums[i]%space]+=1
            index[nums[i]%space] = nums[i] if nums[i] < index[nums[i]%space] or index[nums[i]%space] == 0 else index[nums[i]%space]
            
        for k, v in budget.items():
            if v > max_ or (v == max_ and index[k] < max_i):
                max_ = v
                max_i = index[k]
                
        return max_i
        
s = Solution()
# print(s.destroyTargets([1,5,3,2,2], 10000))
print(s.destroyTargets([3,7,8,1,1,5], 2))
