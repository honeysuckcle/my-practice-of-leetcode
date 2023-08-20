def nodeDistance(g_nodes, g_from, g_to):
    # Write your code here
    in_cycle = []
    ans = [0] * (g_nodes+1)
    graph = [[0 for _ in range(g_nodes+1)] for _ in range(g_nodes+1)]
    for i in range(len(g_from)):
        graph[g_from[i]][g_to[i]] = 1
        graph[g_to[i]][g_from[i]] = 1
    # find cycle
    queue = [[1, [1]]]
    while queue:
        node, path = queue.pop()
        flag = False
        for i, e in enumerate(graph[node]):
            if e == 1:
                if i not in path:
                    queue.append([i, path+[i]])
                elif i != path[-2]:
                    # find it
                    flag = True
                    j = 0
                    while path[j] != i:
                        j += 1
                    in_cycle = path[j:]
                    for j in range(len(path)-1):
                        graph[path[j]][path[j+1]] = 0
                        graph[path[j+1]][path[j]] = 0
                    break
        if flag:
            break
    
    # get ans
    for i in range(1, g_nodes+1):
        if i in in_cycle:
            ans[i] = 0
        else:
            stack = [[i, 0]]
            visited = []
            while stack:
                node, l = stack.pop()
                if node in in_cycle:
                    ans[i] = l
                    break
                if node not in visited:
                    visited.append(node)
                    for j, e in enumerate(graph[node]):
                        if e == 1:
                            stack.append([j, l+1])
            
    return ans[1:]
        
print(nodeDistance(4, [1, 4, 4 ,1], [3,3,2,2]))