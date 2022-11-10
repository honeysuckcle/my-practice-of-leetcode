from array import array
from collections import defaultdict
from typing import List
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dict_ = defaultdict(list)
        n = len(groupSizes)
        for i in range(n):
            dict_[groupSizes[i]].append(i)
        res = []
        for k, v in dict_.items():
            count = 0
            while k*count < len(v):
                res.append(v[k*count:k*count+k])
                count += 1
        return res

s = Solution().groupThePeople([3,3,3,3,3,1,3])
print(s)