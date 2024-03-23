from bisect import bisect_left
n = int(input())
arr = []
for _ in range(n):
    ai, bi = list(map(int, input().split()))
    arr.append((ai, bi))
arr.sort(key=lambda x: x[0])
new_arr = []
x = 0
for i in range(n):
    if arr[i][1] > x:
        new_arr.append(arr[i])
        x = arr[i][1]
q = int(input())
for _ in range(q):
    ans = -1
    x = int(input())
    # for a, b in arr:
    #     if a <= x:
    #         ans = max(ans, b)
    # print(ans)

    l, r = 0, len(new_arr)-1
    while l < r:
        mid = (l+r+1) // 2
        if new_arr[mid][0] <= x:
            l = mid
        else:
            r = mid - 1
    if new_arr[l][0] > x:
        print(-1)
    else:
        print(new_arr[l][1])

