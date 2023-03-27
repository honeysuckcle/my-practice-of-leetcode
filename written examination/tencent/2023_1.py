import math
t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))
    p = 0
    dx = (b-a) / 499
    xi = a
    while xi < b:
        p += math.sin(math.sqrt(xi)) / (5.68 * dx)
        xi += dx
    if p > 0.5:
        print(p, 1)
    else:
        print(p, 0)