class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def get_bool(ch):
            if ch == 'f':
                return False
            if ch == 't':
                return True
        stack = []
        num = []
        for x in expression:
            if x == '!' or x == '(' or x == '|' or x == '&' or x == ',':
                stack.append(x)
            elif x == 'f' or x == 't':
                num.append(get_bool(x))
            elif x == ')':
                op = stack.pop()
                counter = 0
                while stack and op != '(':
                    counter += 1
                    op = stack.pop()
                op = stack.pop()
                if op == '&':
                    res = True
                else:
                    res = False
                for i in range(counter+1):
                    if op == '&':
                        res = num.pop() and res
                    elif op == '|':
                        res = num.pop() or res
                    elif op == '!':
                        res = not num.pop()
                num.append(res)
        return num[-1]

s = Solution()
print(s.parseBoolExpr("!(&(!(&(f)),&(t),|(f,f,t)))"))