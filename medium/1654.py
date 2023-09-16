from typing import List
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        f = set(forbidden)
        queue = [(0, 0, False)]
        visited = set()
        while queue:
            p, step, can_left = queue[0]
            del queue[0]
            if p == x:
                return step
            if a > b and p > x+b:
                continue
            if (p, can_left) not in visited:
                visited.add((p, can_left))
                if p + a not in f:
                    queue.append((p+a, step + 1, True))
                if can_left and p - b not in f and p-b > 0:
                    queue.append((p-b, step + 1, False))
        return -1

s = Solution()
print(s.minimumJumps(forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7))