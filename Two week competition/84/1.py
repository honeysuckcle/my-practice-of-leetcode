from collections import defaultdict
from typing import List
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dict_ = defaultdict(int)
        for it in items1:
            dict_[it[0]] += it[1]
        for it in items2:
            dict_[it[0]] += it[1]
        
        res = []
        for k, v in dict_.items():
            res.append([k,v])
        
        res.sort(key=lambda x:x[0])
        return res

print(Solution().mergeSimilarItems([[1,1],[4,5],[3,8]], [[3,1],[1,5]]))