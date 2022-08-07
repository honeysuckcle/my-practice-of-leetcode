from typing import List
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        len_ = len(words)
        res = []
        for i in range(len_):
            for j in range(i, len_):
                if words[j].find(words[i]) != -1:
                    res.append(words[i])
                    break
        return res

Solution().stringMatching(["mass","as","hero","superhero"])