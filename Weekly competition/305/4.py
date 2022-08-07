from typing import List
def longestIdealString(s: str, k: int) -> int:
    l = len(s)
    dp = [[0 for i in range(l)] for i in range(l)]
    dp_ch = [[None for i in range(l)] for i in range(l)]
    for i in range(l):
        dp[i][i] = 1
        dp_ch[i][i] = s[i]

    for j in range(l):
        for i in range(j):
            dis = abs(ord(s[j]) - ord(dp_ch[i][j-1]))
            if dis <= k:
                dp[i][j] = dp[i][j-1] + 1
                dp_ch[i][j] = s[j]
            else:
                dp[i][j] = dp[i][j-1]
                dp_ch[i][j] = dp_ch[i][j-1]
    
    res = 0
    for i in range(l):
        if dp[i][l-1] > res:
            res = dp[i][l-1]
    return res

print(longestIdealString("eduktdb", 15))

