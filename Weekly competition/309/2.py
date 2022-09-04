class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        dp = [{x:0 for x in range(startPos-k, startPos+k+1)} for _ in range(k+1)]
        dp[0][endPos] = 1
        for i in range(1, k+1):
            for x in range(startPos-k+1, startPos+k):
                dp[i][x] = dp[i-1][x-1] + dp[i-1][x+1]
        return dp[k][startPos]
            
s = Solution()
print(s.numberOfWays(1,2,3))