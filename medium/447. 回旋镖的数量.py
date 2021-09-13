"""
Date: 2021/9/13 Mon
算法：哈希表 + 枚举
时间复杂度：O(n^2)
"""
from typing import List
from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for i in points:
            hashTable = defaultdict(int)
            for j in points:
                dis = (i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2 #为了方便计算，直接使用平方和
                hashTable[dis] += 1
            for x in hashTable.values():
                ans += x * (x - 1) # 排列组合A_{x}^{2}，如果x=1 结果为0
        return ans