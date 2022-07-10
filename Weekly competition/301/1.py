from typing import List
def fillCups(amount: List[int]) -> int:
    res = 0
    while(True):
        amount.sort(reverse=True)
        if amount[1] > 0:
            amount[0] -= 1
            amount[1] -= 1
            res += 1
        else:
            res += amount[0]
            return res
    return res

res = fillCups([5,4,4])
print(res)