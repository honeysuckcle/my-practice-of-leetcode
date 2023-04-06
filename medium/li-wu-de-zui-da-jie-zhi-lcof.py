from typing import List
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        def dfs(i, j, visited, gift):
            nonlocal ans
            if i >= 0 and i < m and j >= 0 and j < n and visited[i][j] == 0:
                visited[i][j] = 1
                if i == m-1 and j  == n-1:
                    ans = max(gift + grid[i][j], ans)
                dfs(i+1, j , visited, gift+grid[i][j])
                dfs(i, j+1, visited, gift + grid[i][j])
        
        dfs(0, 0, [[0 for _ in range(n)] for _ in range(m)], 0)
        return ans
    
s = Solution()
print(s.maxValue([[1,3,1],[1,5,1],[4,2,1]]))

