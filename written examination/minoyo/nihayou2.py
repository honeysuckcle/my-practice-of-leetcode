
n = int(input())
values = list(map(int, input().split()))
values = [0] + values
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n-1):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

dep = [1] * (n+1)
ans = 0
queue = [[1, 1]]
while(queue):
    node, d = queue[0]
    del queue[0]
    ans += values[node] * d
    for i in range(1, n+1):
        if graph[node][i]:
            graph[i][node] = 0
            dep[i] = d+1
            queue.append([i, d+1])

max_tmp = 0
for i in range(2, n+1):
    tmp = 0
    queue = [i]
    while queue:
        node = queue[0]
        del queue[0]
        tmp += values[node] * (dep[node] - 2)
        for j in range(2, n+1):
            if graph[node][j]:
                queue.append(j)
    max_tmp = max(max_tmp, tmp)

print(ans-max_tmp)


