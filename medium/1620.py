import typing


from typing import List
from math import inf, sqrt, pow
class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        x1, x2, y1, y2 = inf, -inf, inf, -inf
        for i, j ,_ in towers:
            if i-radius < x1:
                x1 = max(0, i-radius)
            if i + radius > x2:
                x2 = max(0, i + radius)
            if j - radius < y1:
                y1 = max(0, j-radius)
            if j + radius > y2:
                y2 = max(0, j+radius)
        def d(point1, point2):
            return sqrt(pow(point1[0]-point2[0], 2) + pow(point1[1]-point2[1], 2))
        def signal(point):
            res = 0
            for i, j, q in towers:
                dis = d([i,j], point)
                if dis <= radius:
                    res += q // (1+d([i,j], point))
            return res

        res = [0,0]
        max_signal = -inf
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                s = signal([i,j])
                if s > max_signal:
                    max_signal = s 
                    res = [i,j]
                elif s == max_signal and i >=0 and j>=0 and (i<res[0] or (i==res[0] and j < res[1])):
                    res = [i,j]
        if max_signal == 0:
            return [0,0]
        return res

s = Solution()
print(s.bestCoordinate([[9,3,41],[43,43,7],[46,0,24],[36,22,36],[38,28,9],[40,20,7],[40,30,42],[41,50,49],[38,42,0],[23,28,18],[29,50,17],[23,42,9],[34,18,4],[21,30,38],[40,37,2],[35,29,50],[49,45,22],[47,6,0],[31,41,8],[21,10,29],[15,4,27],[43,35,47],[6,43,41],[7,3,27],[6,34,36],[26,25,21],[22,21,20],[29,8,29],[12,16,28]],37))