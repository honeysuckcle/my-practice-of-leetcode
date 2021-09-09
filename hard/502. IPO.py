"""
Date: 2021/9/8
算法：利用最大堆的贪心算法
时间复杂度：O((n+k)logn)
空间复杂度：O(n)
本题解题方式类似于“银行家算法”
遇到的问题：
一开始读题的时候没有想明白“净利润”的含义，也就是说完成一个任务是不需要计算资本的消耗的
又因为净利润一定大于零，所以不用担心做完一个项目导致资本减少，从而可能做不了之前进入队列的一些项目

用到的一些函数
1. nlargest() 
    https://www.cnblogs.com/chuanxiaopang/p/10222872.html
2. heappush()
   heappop() 弹出最小值
    https://www.jianshu.com/p/801318c77ab5
3. sort() 默认升序
    https://www.runoob.com/python/att-list-sort.html

"""
from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= max(capital):
            return w + sum(heapq.nlargest(k, profits))
        
        curr = 0
        n = len(profits)
        arr = []
        for x in range(n):
            arr.append((capital[x], profits[x]))

        arr.sort(key = lambda x: x[0])
        pq = []

        for _ in range(k):
            while curr < n and arr[curr][0] <= w:
                heapq.heappush(pq, -1 * arr[curr][1])
                curr += 1
            
            if pq:
                w -= heapq.heappop(pq)
            else:
                break
        return w