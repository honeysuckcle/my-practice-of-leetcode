class Solution:
    def compressString(self , param: str) -> str:
        # write code here
        cnt = 0
        n = len(param)
        pre = None
        ans = ''
        for i in range(n):
            if param[i] == pre:
                cnt += 1
            else:
                if pre is not None:
                    ans += pre
                if cnt > 1:
                    ans += str(cnt)
                cnt = 1
                pre = param[i]
        ans += pre
        if cnt > 1:
            ans += str(cnt)

        return 
    
print(Solution().compressString("aabcccccaaa"))