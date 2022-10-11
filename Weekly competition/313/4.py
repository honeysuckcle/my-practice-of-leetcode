class Solution:
    def deleteString(self, s: str) -> int:
        dp = [1] * len(s)
        for n in range(len(s) - 1, -1, -1):
            res = 0
            for i in range(1, int((len(s)-n)/2)+1):
                if s[n:i+n] == s[i+n:2*i+n] and dp[n+i] > res:
                    res = dp[n+i]
            dp[n] = res+1
        return dp[0]

s = Solution()
print(s.deleteString("aaabaab"))