n, H, A = list(map(int, input().split()))
h_arr = list(map(int, input().split()))
a_arr = list(map(int, input().split()))
pair = list(zip(h_arr, a_arr))
pair.sort(key=lambda x: x[0])
dp = [1] * n
ans = 0
for i in range(n):
    for j in range(i):
        if pair[j][1] < pair[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)
    if pair[i][0] < H and pair[i][1] < A:
        ans = max(ans, dp[i])

print(ans)