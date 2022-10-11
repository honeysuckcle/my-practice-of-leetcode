from typing import List
class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        m = len(mat)
        n = len(mat[0])
        choose_row = []
        for i in range(m):
            nums_row = sum(mat[i])
            if nums_row != 0:
                choose_row.append(i)
                for j in range(n):
                    mat[i][j] = mat[i][j] / nums_row
        choose = [0]
        nums_col = []
        for j in range(n):
            num = 0
            for i in range(m):
                num += mat[i][j]
            nums_col.append(num)
            if len(choose) < cols + 1:
                choose.append(j)
                curr = len(choose) -1
                father = int(curr/2)
                while father > 0:
                    if nums_col[choose[father]] > nums_col[choose[curr]]:
                        temp = choose[curr]
                        choose[curr] = choose[father]
                        choose[father] = temp
                        curr = father
                        father = int(curr/2)
                    else:
                        break
            elif  num > nums_col[choose[1]]:
                choose[1] = j
                curr = 1
                left = curr *2
                right = left +1
                while left < cols+1:
                    change = left
                    if right < cols+1 and nums_col[choose[right]] < nums_col[choose[left]]:
                            change = right
                    if nums_col[choose[change]] < nums_col[choose[curr]]:
                        temp = choose[curr]
                        choose[curr] = choose[change]
                        choose[change] = temp
                        curr = change
                    else:
                        break
        res = m - len(choose_row)
        for i in range(len(choose_row)):
            sum_ = 0
            for j in range(1, cols+1):
                sum_ += mat[choose_row[i]][choose[j]]
            if sum_ == 1:
                res += 1
        return res

s = Solution()
test1 = [[0,0,0],[1,0,1],[0,1,1],[0,0,1]]
col1 = 2
test2 = [[1],[0]]
cols2 = 1
print(s.maximumRows(test1, col1))
print(s.maximumRows([[1,0,1,0],[1,0,1,0],[0,1,1,1],[0,1,0,0]], 3))