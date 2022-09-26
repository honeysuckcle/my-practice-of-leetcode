import enum
from typing import List
from collections import Counter
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        map_ = [[-1 for _ in range(n)] for _ in range(n)]
        size = Counter()
        cnt = 0
        def dfs(x,y,t):
            map_[x][y] = t
            size[t] += 1
            for i, j in (x+1, y), (x-1, y), (x, y-1), (x, y+1):
                if i>=0 and i <n and j>=0 and j < n and grid[i][j] == 1 and map_[i][j] == -1:
                    dfs(i,j,t)


        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and map_[i][j] == -1:
                    dfs(i,j,cnt)
                    cnt += 1
        
    
        res = max(size.values(), default=0)
        
        def area(x, y):
            indexs = set()
            ans = 0
            # up
            if x-1>=0:
                indexs.add(map_[x-1][y])
            # left
            if y-1>=0:
                indexs.add(map_[x][y-1])
            # down
            if x+1 < n:
                indexs.add(map_[x+1][y])
            # right
            if y+1 <n:
                indexs.add(map_[x][y+1])
            for i in indexs:
                if i != -1:
                    ans += size[i]
            return ans+1

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    a = area(i, j)
                    if a > res:
                        res = a
        return res

s = Solution()
print(s.largestIsland([[0,0],[1,1]]))


                    






