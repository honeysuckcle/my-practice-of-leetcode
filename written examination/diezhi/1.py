from math import inf
n = int(input())
nums = list(map(int, input().split()))

dp = [inf] * n
dp[0] = 0

for i in range(n):
    for j in range(1, 1 + nums[i]):
        if i+j < n:
            dp[i+j] = min(dp[i+j], dp[i] + 1)
        else:
            break

print(dp[-1])
