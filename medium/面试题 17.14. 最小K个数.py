
"""
Date: 2021/9/3
也可以使用堆排序
"""
from typing import List
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]