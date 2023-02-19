from typing import List
from collections import Counter
class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        def yinzi(num):
            ans = []
            for i in range(2, num+1):
                if num % i == 0:
                    ans.append(i)
            return ans
        yinzi_list = list(map(yinzi, nums))
        def is_square(i):
            for j in yinzi_list[i]:
                if nums[i] % (j*j) == 0:
                    return True
            return False
        
        def can_join(arr1, arr2):
            for i in arr1:
                if i in arr2:
                    return False
            return True
        
        def dfs(i, path, cnt):
            if i == n:
                if cnt == 0:
                    return 0
                return 1
            else:
                if is_square(i):
                    return dfs(i+1, path, cnt)
                elif can_join(yinzi_list[i], path):
                    return dfs(i+1, set(list(path)+yinzi_list[i]), cnt+1) + dfs(i+1, path,cnt)
                else:
                    return dfs(i+1, path,cnt)
        ans = dfs(0, set(), 0)
        return ans

s = Solution()
print(s.squareFreeSubsets([1]))