from typing import List
import heapq

class Node:
    def __init__(self, i, j, s) -> None:
        self.i = i
        self.j = j
        self.s = s
    def __lt__(self, other):
        return self.s > other.s or (self.s == other.s and self.i + self.j > other.i + other.j)

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        thief = []
        safe = [[m+n for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    safe[i][j] = 0
                    thief.append([i, j, 0])
        
        
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # for i in range(m):
        #     for j in range(n):
        #         for ti, tj in thief:
        #             safe[i][j] = min(abs(ti-i)+abs(tj-j), safe[i][j])

        while thief:
            i, j, d = thief[0]
            del thief[0]
            for di, dj in dirs:
                if i+di >= 0 and i+di < m and j+dj >= 0 and j+dj < n and safe[i+di][j+dj] == 2*n:
                    safe[i+di][j+dj] = d+1
                    thief.append((i+di, j+dj, d+1))

        # ans = [[0 for _ in range(n)] for _ in range(m)]
        visited = [[0 for _ in range(n)] for _ in range(m)]
        queue = [Node(0, 0, safe[0][0])]
        visited[0][0] = 1
        heapq.heapify(queue)
        while queue:
            node = heapq.heappop(queue)
            i, j, s = node.i, node.j, node.s
            if i == m-1 and j == n-1:
                return s
            
            for di, dj in dirs:
                if i+di >= 0 and i+di < m and j+dj >= 0 and j+dj < n and visited[i+di][j+dj] == 0:
                    visited[i+di][j+dj] = 1
                    heapq.heappush(queue, Node(i+di, j+dj, min(s, safe[i+di][j+dj])))
    
        return 0
    
s =Solution()
print(s.maximumSafenessFactor([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]))