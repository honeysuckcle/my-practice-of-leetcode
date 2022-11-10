class Solution:
    def solveEquation(self, equation: str) -> str:
        x = 0
        num = 0
        left, right = equation.split('=')
        i = 0
        last_i = 0
        while i < len(left):
            op_num = ''
            if left[i] == '+':
                op_num = left[last_i:i]
                last_i = i+1
            elif left[i] == '-':
                op_num = left[last_i:i]
                last_i = i
            elif i == len(left) - 1:
                op_num = left[last_i:]
            if len(op_num) > 0:
                if op_num[-1] == 'x':
                    xishu = op_num[:-1]
                    if xishu == '-' or xishu == '':
                        xishu += '1'
                    x += int(xishu)
                else:
                    num += -1 * int(op_num)
            i+=1
        last_i = 0
        i = 0
        while i < len(right):
            op_num = ''
            if right[i] == '+':
                op_num = right[last_i:i]
                last_i = i+1
            elif right[i] == '-':
                op_num = right[last_i:i]
                last_i = i
            elif i == len(right) - 1:
                op_num = right[last_i:]
            if len(op_num) > 0:
                if op_num[-1] == 'x':
                    xishu = op_num[:-1]
                    if xishu == '-' or xishu == '':
                        xishu += '1'
                    x += -1 * int(xishu)
                else:
                    num += int(op_num)
            i+=1
        if x == 0:
            if num == 0:
                return 'Infinite solutions'
            else:
                return 'No solution'
        
        return 'x=' + str(int(num/x))



Solution().solveEquation("x+5-3+x=6+x-2")