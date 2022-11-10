from typing import List
def arithmeticTriplets(nums: List[int], diff: int) -> int:
    res = 0
    l = len(nums)
    for i in range(l):
        for j in range(i+1, l):
            for k in range(j+1, l):
                if nums[j] - nums[i] == diff and nums[k]- nums[j] == diff:
                    res += 1
    return res