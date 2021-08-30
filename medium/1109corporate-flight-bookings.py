"""
Date: 2021/8/31
"""
from typing import List

def corpFlightBookings(bookings: List[List[int]], n: int) -> List[int]:
    dif = [0] * (n + 1)
    for x in bookings:
        dif[x[0]] += x[2]
        if x[1] < n:
            dif[x[1] + 1] -= x[2]
    
    for i in range(n):
        dif[i+1] += dif[i]

    dif.remove(0)
    return dif

print (corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]], 5))
