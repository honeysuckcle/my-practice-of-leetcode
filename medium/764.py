from typing import List
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[1 for _ in range(n)] for _ in range(n)]
        dp = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(n)]
        res = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(len(mines)):
            x, y = mines[i]
            grid[x][y] = 0
    
        for d in range(n):
            # top
            for i in range(n):
                if grid[d][i] == 1:
                    if d-1>=0:
                        dp[d][i][0] = dp[d-1][i][0] + 1
                    else:
                        dp[d][i][0] = 1
            # left
            for i in range(n):
                if grid[i][d] == 1:
                    if d-1>=0:
                        dp[i][d][1] = dp[i][d-1][1] + 1
                    else:
                        dp[i][d][1] = 1
            # bottom
            for i in range(n):
                if grid[n-d-1][i] == 1:
                    if n-d<n:
                        dp[n-d-1][i][2] = dp[n-d][i][2] + 1
                    else:
                        dp[n-d-1][i][2] = 1
            # right
            for i in range(n):
                if grid[i][n-d-1] == 1:
                    if n-d<n:
                        dp[i][n-d-1][3] = dp[i][n-d][3] + 1
                    else:
                        dp[i][n-d-1][3] = 1
        ans = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    res[i][j] = min(dp[i][j][d] for d in range(4))
                    if res[i][j] > ans:
                        ans = res[i][j]

        return ans

s = Solution()
print(s.orderOfLargestPlusSign(2, [[0,0],[0,1],[1,0]]))