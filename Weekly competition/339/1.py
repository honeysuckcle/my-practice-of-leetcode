class Solution:
    def isbalance(self, s):
        n = len(s)
        if n % 2 != 0:
            return False
        for i in range(n//2):
            if s[i] != '0':
                return False
        for i in range(n//2, n):
            if s[i] != '1':
                return False
        return True
    def findTheLongestBalancedSubstring(self, s: str) -> int:
            
        n = len(s)
        ans = 0
        for l in range(2, n+1, 2):
            for i in range(n-l+1):
                if self.isbalance(s[i:i+l]):
                    ans = max(ans, l)
        return ans
                
print(Solution().findTheLongestBalancedSubstring("01000111"))