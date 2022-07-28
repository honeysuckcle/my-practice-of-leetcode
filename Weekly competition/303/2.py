def equalPairs(grid) -> int:
    n = len(grid)
    res = 0
    for i in range(n):
        for j in range(n):
            flag = True
            for k in range(n):
                if grid[i][k] != grid[k][j]:
                    flag = False
                    continue
            if flag:
                res += 1
    return res

print(equalPairs([[3,2,1],[1,7,6],[2,7,7]]))