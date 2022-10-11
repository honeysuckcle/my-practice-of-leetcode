class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        zhiweishu = str(bin(num2)).count('1')
        n1 = str(bin(num1))[2:]
        res = list('0'*len(n1))
        if len(n1) < zhiweishu:
            return int('1'*zhiweishu,2)

        for i in range(len(n1)):
            if zhiweishu > 0 and n1[i] == '1':
                res[i] = n1[i]
                zhiweishu -= 1
        p1 = len(n1) - 1
        while zhiweishu > 0:
            if res[p1] == '1':
                p1 -= 1
                continue
            else:
                res[p1] = '1'
                zhiweishu -= 1
                p1 -= 1
        return int(''.join(res),2)


            
                    

s = Solution()
print(s.minimizeXor(25, 72))