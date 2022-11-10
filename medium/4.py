class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        max_left = 0
        max_right = 0
        l = len(s)
        if l < 2:
            return s
        dp = [[False for _ in range(l)] for _ in range(l)]
        for L in range(1, l):
            for i in range(l):
                j = i + L -1
                if j < l:
                    if s[i] == s[j]:
                        if L <= 3:
                            dp[i][j] = True
                        else:
                            dp[i][j] = dp[i+1][j-1]
                    else:
                        dp[i][j] = False
                
                    if dp[i][j] == True and L > max_len:
                        max_len = L
                        max_left = i
                        max_right = j + 1
        return s[max_left:max_right]

Solution().longestPalindrome('bb')