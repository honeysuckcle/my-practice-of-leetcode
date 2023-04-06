from typing import List
from collections import defaultdict
from math import inf
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        ans = inf
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        visited = [0] * n
        for i in range(n):
            if visited[i] == 0:
                stack = [(i,set())]
                while stack:
                    j, path = stack.pop()
                    if j in path and len(path) > 2:
                        ans = min(ans, len(path) + 1)
                    if visited[j] == 0:
                        visited[j] = 1
                        for k in graph[j]:
                            stack.append((k, path | set([j])))
        return ans if ans != inf else -1

print(Solution().findShortestCycle(4, [[0,1],[0,2]]))                    
                    
                
                