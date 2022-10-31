from typing import List
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        n = queries[0]
        res = []
        for i in range(len(queries)):
            for j in range(len(dictionary)):
                count = 0
                flag = True
                for k in range(n):
                    if queries[i][k] != dictionary[j][k]:
                        count += 1
                    if count > 2:
                        flag = False
                        break
                if flag:
                    res.append(queries[i])
                    break
        return res

                