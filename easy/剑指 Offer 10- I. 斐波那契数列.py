"""
Date: 2021/9/4
DP + 滚动数组
时间复杂度O(n)
空间复杂度O(1)
"""
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        mod = 10 ** 9 + 7
        p, q, r = 0, 1, 1
        for i in range(2, n):
            p = q
            q = r
            r = (p + q) % mod
        return r

"""
矩阵快速幂算法
时间复杂度O(logn)

class Solution:
    def fib(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n < 2:
            return n

        def multiply(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
            c = [[0, 0], [0, 0]]
            for i in range(2):
                for j in range(2):
                    c[i][j] = (a[i][0] * b[0][j] + a[i][1] * b[1][j]) % MOD
            return c

        def matrix_pow(a: List[List[int]], n: int) -> List[List[int]]:
            ret = [[1, 0], [0, 1]]
            while n > 0:
                if n & 1:
                    ret = multiply(ret, a)
                n >>= 1
                a = multiply(a, a)
            return ret

        res = matrix_pow([[1, 1], [1, 0]], n - 1)
        return res[0][0]

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/solution/fei-bo-na-qi-shu-lie-by-leetcode-solutio-hbss/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""