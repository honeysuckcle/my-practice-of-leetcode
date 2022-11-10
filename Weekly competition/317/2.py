from collections import defaultdict
from typing import List
class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        n = len(creators)
        res = []
        max_view = 0
        max_k = []
        id_dict = {}
        pop_dict = defaultdict(int)
        for i in range(n):
            k = creators[i]
            pop_dict[k] += views[i]
            if id_dict.get(k) is None:
                id_dict[k] = i
            else:
                id = id_dict[k]
                if views[i] > views[id]:
                    id_dict[k] = i
                elif views[i] == views[id]:
                    id_dict[k] = i if ids[i] < ids[id] else id
        for k, v in pop_dict.items():
            if v > max_view:
                max_view = v
                max_k = [k]
            elif v == max_view:
                max_k.append(k)
        for k in max_k:
            res.append([k, ids[id_dict[k]]])
        return res
        



