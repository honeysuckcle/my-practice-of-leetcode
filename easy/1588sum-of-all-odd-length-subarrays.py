"""
Date: 2021/8/29
"""
from typing import List

def sumOddLengthSubarrays(arr: List[int]) -> int:
    length = len(arr)
    count = [0 for x in range(length)]
    # print(count)
    for i in range(length):
        for j in range(1, length - i + 1, 2):
            # print(i, j)
            for k in range(i, i + j):
                count[k] += 1
    # print(count)
    ans = 0
    for i in range(length):
        ans += count[i] * arr[i]

    return ans

ans = sumOddLengthSubarrays([1,4,2,5,3])
print(ans)
