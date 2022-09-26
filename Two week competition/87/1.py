from typing import List
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days =  [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def getdate(s:str):
            return s[:2], s[3:]
        def getdayNum(start, end):
            if start == end:
                return 1
            if isEarly(end, start):
                return 0
            startM, startD = getdate(start)
            endM, endD = getdate(end)
            if startM == endM:
                return endD - startD
            res = days[startM] - startD + 1
            for i in range(startM+1, endM):
                res += days[i]
            res += endD
            return res
        def isEarly(d1, d2):
            d1M, d1D = getdate(d1)
            d2M, d2D = getdate(d2)
            if d1M < d2M:
                return True
            elif d1M > d2M:
                return False
            elif d1D < d2D:
                return True
            else:
                return False
        if isEarly(arriveAlice, arriveBob):
            if isEarly(leaveAlice, leaveBob):
                return getdayNum(arriveBob, leaveAlice)
            else:
                return getdayNum(arriveBob, leaveBob)
        else:
            if isEarly(leaveAlice, leaveBob):
                return getdayNum(arriveAlice, leaveAlice)
            else:
                return getdayNum(arriveAlice, leaveBob)