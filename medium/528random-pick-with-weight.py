"""
Date: 2021/8/30
"""
from typing import List
import random

"""
# 超时
class Solution:
    
    def __init__(self, w: List[int]):
        self.mid = []
        for i in range(len(w)):
            for j in range(w[i]):
                self.mid.append(i)
        self.num = len(self.mid)

    def pickIndex(self) -> int:
        n = random.randint(0, self.num - 1)
        return self.mid[n]

"""
import itertools
import bisect

class Solution:
    
    def __init__(self, w: List[int]):
        self.pre = list(itertools.accumulate(w))
        self.total = sum(w)

    def pickIndex(self) -> int:
        n = random.randint(1, self.total)
        return bisect.bisect_left(self.pre, n)




# Your Solution object will be instantiated and called as such:
obj = Solution([1,3])
param_1 = obj.pickIndex()
print(param_1)