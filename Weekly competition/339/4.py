from typing import List
class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        dp = [-1] * n
        queue = [p]
        dp[p] = 0
        canReverse = [1] * n
        visited = [0] * n
        for b in banned:
            canReverse[b] = 0
            visited[b] = 1
        while queue:
            index = queue[0]
            del queue[0]
            if visited[index] == 0:
                visited[index] = 1
                for i in range(max(index-k+1, k-1-index), min(index+k, index-(k-1)+2*(n-index-1)+1), 2):
                    if i >= 0 and i < n and i != index and canReverse[i] and visited[i] == 0:
                        if dp[i] == -1:
                            dp[i] = dp[index] + 1
                        queue.append(i)
        return dp
print(Solution().minReverseOperations(8, 6, [0], 5))