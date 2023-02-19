from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        queue = []
        m = len(board)
        n = len(board[0])
        l = len(word)
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        return True
                    queue.append([i+1,j,1,[[i,j]]])
                    queue.append([i-1,j,1,[[i,j]]])
                    queue.append([i,j-1,1,[[i,j]]])
                    queue.append([i,j+1,1,[[i,j]]])
        while queue:
            i, j, k, v = queue[0]
            del queue[0]
            if i >=0 and i < m and j >=0 and j <n and k < l and board[i][j] == word[k] and [i,j] not in v:
                if k == l-1:
                    return True
                path = v.copy()
                path.append([i, j])
                queue.append([i+1,j,k+1, path])
                queue.append([i-1,j,k+1, path])
                queue.append([i,j-1,k+1, path])
                queue.append([i,j+1,k+1, path])
        return False

s = Solution()
print(s.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))