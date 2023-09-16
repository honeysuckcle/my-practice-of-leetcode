T = int(input())
for _ in range(T):
    n, a, b = list(map(int, input().split()))
    if abs(a-b)+1 > n:
        print(-1)
    else:
        print((n+a+b-1)//2)