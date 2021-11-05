"""
Date: 2021/9/29
思路：
首先想到的是计算平均数，用来判断能否实现每个洗衣机内的衣物数量相同
之后将多于平均数的洗衣机的衣服往相邻洗衣机中移动
直到每个洗衣机内的衣服都等于平均数

但是，上述算法有问题
例如：处理[0,0,0,4]
只需要3步
1 [0, 0, 1, 3]
2 [0, 1, 1, 2]
3 [1, 1, 1, 1]

但是上述算法需要5步
1 [0, 0, 1, 3]
2 [0, 0, 2, 2]
3 [0, 1, 2, 1]
4 [0, 2, 1, 1]
5 [1, 1, 1, 1]

问题在于1也要往左边移动
但并没有想到好的解题方法

于是看了精妙的官方解题思路，看懂了怎么做，但还不懂为什么。
TODO 理解最优解的计算原理
"""

from typing import List, TextIO

def findMinMoves(machines: List[int]) -> int:
        # total = 0
        # for i in machines:
        #     total += i
        total = sum(machines)

        n = len(machines)

        avg = total/n
        if avg != int(avg):
            return -1
        
        ans, s = 0, 0
        for num in machines:
            num -= avg
            s += num
            ans = max(ans, abs(s), num)
        return int(ans)



print(findMinMoves([0,0,0,4]))