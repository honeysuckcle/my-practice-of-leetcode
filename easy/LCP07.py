from typing import List
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v in relation:
            graph[u].append(v)
        dp = [[0 for _ in range(n)] for _ in range(k)]
        for i in graph[0]:
            dp[0][i] = 1
        for i in range(1, k):
            for j in range(n):
                for t in range(n):
                    if t in graph[j]:
                        dp[i][t] += dp[i-1][j]
        return dp[k-1][n-1]

s = Solution()
print(s.numWays(3, [[0,2],[0,1],[1,2],[2,1],[2,0],[1,0]], 1))