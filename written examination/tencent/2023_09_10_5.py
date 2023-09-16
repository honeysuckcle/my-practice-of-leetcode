def gongsheng(a, b, k):
    m, n = len(a), len(b)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] >= k:
                    return True
    return False
    
n, k = list(map(int, input().split()))
s_arr = []
for _ in range(n):
    s_arr.append(input())
remove_arr = list(map(int, input().split()))
fa = [i for i in range(n)]
def find(x):
    while fa[x] != x:
        x = fa[x]
    return x
def add(x, y):
    fa[find(x)] = find(y)
    
ans = [0]
added = []
for i in range(n-1, -1, -1):
    cur = remove_arr[i] - 1
    for y in added:
        if gongsheng(s_arr[cur], s_arr[y], k):
            add(cur, y)
    added.append(cur)
    num = set()
    for x in added:
        num.add(find(x))
    num = len(num)
    ans.append(num)
    
ans.reverse()
for x in ans:
    print(x)