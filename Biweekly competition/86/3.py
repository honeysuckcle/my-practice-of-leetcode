class Solution:
    def maximumRows(self, mat, cols: int) -> int:
        ans = 0
        mask = [sum(v << j for j, v in enumerate(row)) for i, row in enumerate(mat)]
        for set in range(1 << len(mat[0])):
            if set.bit_count() == cols:  # 集合的大小等于 cols，符合题目要求
                ans = max(ans, sum(row & set == row for row in mask))  # row & set = row 表示 row 是 set 的子集，所有 1 都被覆盖
        return ans

s = Solution()
print(s.maximumRows([[0,0,0],[1,0,1],[0,1,1],[0,0,1]], 2))