import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    graph = [[0 for i in range(n+1)] for _ in range(n+1)]
    for i in range(n-1):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        u, v = list(map(int, line.split()))
        graph[u][v] = 1
        graph[v][u] = 1
    leaf = []
    ans = ['R'] * (n+1)
    queue = []
    def blue_child(index):
        if index in leaf:
            return 1
        res = 0
        for i in range(1, n+1):
            if graph[i][index] == 1 and ans[i] == 'B':
                res += blue_child(i)
        return res
    for i in range(1, n+1):
        if sum(graph[i]) == 1:
            leaf.append(i)
            ans[i] = 'B'
            for j in range(1, n+1):
                if graph[i][j] == 1 and j not in queue:
                    queue.append(j)
    visited = leaf.copy()
    while len(queue)>0:
        node = queue[0]
        visited.append(node)
        del queue[0]
        if blue_child(node) % 2 == 0:
            ans[node] = 'B'
        for i in range(1, n+1):
            if graph[node][i] == 1 and i not in visited and i not in queue:
                queue.append(i)
    
    print(ans[1:])


    