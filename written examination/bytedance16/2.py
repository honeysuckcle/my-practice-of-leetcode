#coding=utf-8
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.split()))
    pairs = list(zip(range(1,n+1), values))
    a = sorted(pairs, key=lambda x:x[1])
    
    graph = []
    visited = [1]

    for i, ai in a:
        if ai == 1:
            graph.append([1, i])
            visited.append(i)
        else:
            for k in visited:
                if values[k-1] + 1 == ai:
                    graph.append([k, i])
                    visited.append(i)
                    break
    if len(visited) != n:
        print(-1)
    else:
        print(len(graph))
        for g in graph:
            print(str(g[0])+' '+str(g[1]))