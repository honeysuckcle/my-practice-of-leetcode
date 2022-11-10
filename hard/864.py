from typing import List
from math import inf
class Solution:
    def __init__(self):
        self.res = inf
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m = len(grid)
        n = len(grid[0])
        map_ = [[1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        locks = set()
        s = [0,0,0,0]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '#':
                    map_[i][j] = 0
                elif grid[i][j] == '@':
                    s[0] = i
                    s[1] = j
                elif ord(grid[i][j]) >= ord('a') and ord(grid[i][j]) <= ord('z'):
                    map_[i][j] = 2
                elif ord(grid[i][j]) >= ord('A') and ord(grid[i][j]) <= ord('Z'):
                    map_[i][j] = 3
                    locks.add(ord(grid[i][j])- ord('A'))

        def add_key(s, k):
            if s < pow(2, k) or not get_key(s, k):
                s += pow(2, k) 
            return s

        def get_key(s, k):
            if s < pow(2, k):
                return False
            if str(bin(s))[-(k+1)] == '1':
                return True
            return False

        vis = [[[0 for _ in range(pow(2, len(locks)))] for _ in range(n)] for _ in range(m)]
        queue = [s]
        while queue:
            x, y, keys, path = queue[0]
            queue.pop(0) 
            if x <0 or x >= m or y <0 or y>=n or map_[x][y] == 0 or vis[x][y][keys]:
                continue
            if map_[x][y] == 3 and not get_key(keys, ord(grid[x][y]) - ord('A')):
                continue
            if map_[x][y] == 2:

                keys = add_key(keys, ord(grid[x][y]) - ord('a'))
                if keys == pow(2, len(locks)) - 1:
                    if self.res > path:
                        self.res = path
                    continue
            vis[x][y][keys] = 1
            queue.append([x+1, y, keys, path + 1])
            queue.append([x-1, y, keys, path + 1])
            queue.append([x, y+1, keys, path + 1])
            queue.append([x, y-1, keys, path + 1])
        return self.res if self.res != inf else -1

s = Solution()
print(s.shortestPathAllKeys([".#.b.","A.#aB","#d...","@.cC.","D...#"])) 