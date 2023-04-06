from typing import List
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        val_dict = {chr(ord('a') + i - 1): i for i in range(1, 27)}
        
        for i in range(len(chars)):
            val_dict[chars[i]] = vals[i]
        n = len(s)
        i = 0
        j = 0
        sum_ = 0
        ans = 0
        while j < n:
            v = val_dict[s[j]]
            sum_ += v
            ans = max(ans, sum_)
            if sum_ < 0:
                i = j+1
                j = i
                sum_ = 0
            else:
                j += 1
        return max(sum_, ans)
print(Solution().maximumCostSubstring("talaqlt", "tqla", [4,3,3,-2]))