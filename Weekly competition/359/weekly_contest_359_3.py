from typing import List
from collections import defaultdict
class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        dp = [0] * (n+1)
        dic = defaultdict(list)
        for s, e, g in offers:
            dic[e].append((s, g))
        
        for i in range(n):
            dp[i] = max(dp[i-1], dp[i])
            for s, g in dic[i]:
                dp[i] = max(dp[i], dp[s-1]+g)
        return dp[-2]
    
s = Solution()
print(s.maximizeTheProfit(10, [[0,6,5],[2,9,4],[0,9,2],[3,9,3],[1,6,10],[0,1,3],[3,8,9],[4,8,3],[2,6,5],[0,4,6]]))