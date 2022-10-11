from typing import List
def reachableNodes(n: int, edges: List[List[int]], restricted: List[int]) -> int:
    graph = [[] for j in range(n)]
    for e in edges:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    passed = [False for i in range(n)]
    passed[0] = True
    for restr in restricted:
        passed[restr] = True
    res = 1
    stack = [0]
    while len(stack) != 0:
        node = stack.pop()
        for i in graph[node]:
            if passed[i] == False:
                stack.append(i)
                passed[i] = True
                res += 1
    return res


res = reachableNodes(7, [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], [4,5])
print(res)