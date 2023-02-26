# ³¬Ê±
from typing import List
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_grid = max([max(line) for line in grid])
        visited = [[[0] * max(n*m+1, max_grid) for _ in range(n)] for _ in range(m)]
        queue = [(0,0,0)]
        while queue:
            i, j, t= queue[0]
            del queue[0]
            if i < m and i>=0 and j<n and j>=0 and visited[i][j][t] == 0:
                visited[i][j][t] = 1
                if t < grid[i][j]:
                    continue
                if i == m-1 and j == n-1:
                    return t
                queue.append((i+1, j, t+1))
                queue.append((i-1, j, t+1))
                queue.append((i, j+1, t+1))
                queue.append((i, j-1, t+1))
        return -1