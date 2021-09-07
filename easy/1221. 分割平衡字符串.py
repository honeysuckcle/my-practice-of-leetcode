"""
Date: 2021/9/7
贪心算法
因为字符串中L和R的个数是相等的，因此，如果从某一位置进行分割，使得左边是平衡字符串，那么右边也必然是平衡字符串
"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        d = 0
        count = 0
        for i in s:
            if i == 'L':
                d -= 1
            else:
                d += 1
            
            if d == 0:
                count += 1
        return count
