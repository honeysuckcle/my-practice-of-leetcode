from typing import List
from collections import defaultdict
def taskSchedulerII(tasks: List[int], space: int) -> int:
    ddict = defaultdict(int)
    day = 1
    i = 0
    while i < len(tasks):
        last = ddict[tasks[i]]
        if day - last >= space or last == 0:
            day += 1
            ddict[tasks[i]] = day
            i += 1
        else:
            day = last + space
    return day - 1

print(taskSchedulerII([5,8,8,5], 2))