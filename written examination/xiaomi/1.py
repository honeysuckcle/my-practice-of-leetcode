from collections import defaultdict
n, m = list(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append(input())
ans = 0
def conclude(cnt):
    for ch in 'xaom':
        if ch not in cnt:
            return False
        if cnt['i'] < 2:
            return False
    return True
if n < 3 or m < 3:
    print(0)
else:
    for i in range(n-3):
        cnt = defaultdict(int)
        for p in range(3):
            for k in range(3):
                cnt[arr[i+p][k]] += 1
        if conclude(cnt):
            ans += 1
        for j in range(m-3):
            for k in range(3):
                cnt[arr[i+k][j]] -= 1
                cnt[arr[i+k][j+3]] += 1
            if conclude(cnt):
                ans += 1
    print(ans)
                
    