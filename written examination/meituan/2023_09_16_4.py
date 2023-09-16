from heapq import heapify, heappop, heappush
from math import inf
n, m = list(map(int, input().split()))
weight = [[0 for _ in range(n)] for _ in range(n)]
graph = [[0 for _ in range(n)] for _ in range(n)]
idx = [[0 for _ in range(n)] for _ in range(n)]
ans = []
visited = set()
for i in range(m):
    u, v, w, p = list(map(int, input().split()))
    u -= 1
    v -= 1
    idx[u][v] = i+1
    idx[v][u] = i+1
    if p == 1:
        graph[u][v] = w
        graph[v][u] = w
        ans.append(i+1)
        visited.add(u)
        visited.add(v)
    else:
        weight[u][v] = w
        weight[v][u] = w

heap = []
heapify(heap)

for i in range(n):
    for j in range(n):
        if i in visited and j not in visited and weight[i][j] > 0:
            heappush(heap, (weight[i][j], i, j))

while len(visited) < n:
    w, i, j = heappop(heap)
    visited.add(j)
    ans.append(idx[i][j])
    for k in range(n):
        if weight[j][k] > 0 and k not in visited:
            heappush(heap, (weight[j][k], j, k))

print(len(ans))
print(' '.join(list(map(str, ans))))