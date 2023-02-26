# ³¬Ê±
from typing import List
class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        if m == 1:
            return [1]*n
        ans = [0] * n
        sum_ = 0
        for i in range(n):
            sum_ = sum_ * 10 + int(word[i])
            if sum_ % m == 0:
                ans[i] = 1
                sum_ = 0
        return ans