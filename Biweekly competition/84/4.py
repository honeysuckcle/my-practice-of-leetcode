import typing


from typing import List
def minimumReplacement(nums: List[int]) -> int:
    res = 0
    i = len(nums)-2
    while i >= 0:
        if nums[i] > nums[i+1]:
            n = int(nums[i] / nums[i+1])
            if n * nums[i+1] != nums[i]:
                n += 1
            res += n - 1
            nums[i] = int(nums[i] / n)
        i -= 1
    return res

print(minimumReplacement([3,9,3]))