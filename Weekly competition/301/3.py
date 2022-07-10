class Solution:
    def tongji(self, s:str):
        R = []
        L = []
        for i in range(len(s)):
            if s[i] == 'L':
                R.append(i)
            elif s[i] == 'R':
                L.append(i)
        return R, L
                    
            
    def canChange(self, start: str, target: str) -> bool:
        R_s, L_s = self.tongji(start)
        R_t, L_t = self.tongji(target)
        if len(R_s) != len(R_t) or len(L_s) != len(L_t):
            return False
        p1, p2 , 


solution = Solution()
s1 = solution.canChange("_L__R__R_", "L______RR")
s2 = solution.canChange("R_L_", "__LR")
s3 = solution.canChange("L_R_L_R", "L_L_R_R")