from math import inf
n, m = list(map(int, input().split()))
grid = []
xs, ys, xt, yt = list(map(lambda x: int(x)-1, input().split()))
for _ in range(n):
    grid.append(input())
visited = [[0 for _ in range(m)] for _ in range(n)]
queue = [(xs, ys, 0)]
ans = inf
while queue:
    x, y, step = queue[0]
    del queue[0]
    if x == xt and y == yt:
        ans = min(step, ans)
    elif x >= 0 and x < n and y >= 0 and y <m:
        visited[x][y] = 1
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i, j in dirs:
            if x+i >= 0 and x+i < n and y+j >= 0 and y+j <m and grid[x+i][y+j] == '.' and visited[x+i][y+j] == 0:
                queue.append((x+i, y+j, step+1))
        
    
print(ans if ans != inf else -1)