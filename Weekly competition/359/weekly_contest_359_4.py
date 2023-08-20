from collections import defaultdict
from typing import List
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        ans = 0
        dic_l = defaultdict(int)
        dic_k = defaultdict(int)
        dic_i = defaultdict(list)
        arr = [1] * len(nums)
        for i in range(1, len(nums)):
            n = nums[i]
            if nums[i-1] == n:
                arr[i] += arr[i-1]
            else:
                dic_i[nums[i-1]].append(i)
        for i, n in enumerate(nums):
            if dic_k[n] <= k:
                dic_l[n] += 1
                ans = max(ans, dic_l[n])
            else:
                if len(dic_i[n]) > 0:
                    idx = dic_i[n][0]
                    del dic_i[n][0]
                    dic_l[n] -= arr[idx-1] - 1
                    dic_k[n] -= 1
                    ans = max(ans, dic_l[n])
            for ke in dic_k.keys():
                if ke != n and dic_l[ke] > 0:
                    dic_k[ke] += 1
        return ans

s = Solution()
print(s.longestEqualSubarray([3,1,5,3,1,1], 0))