from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n):
        rest = target - nums[i]
        for j in range(i+1, n):
            if nums[j] == rest:
                return [i, j]
    return -1

twoSum([3,2,4], 6)