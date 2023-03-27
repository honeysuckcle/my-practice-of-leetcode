t = input()
t = int(t)
for _ in range(t):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    cur = 1
    idx = 0
    ans = 0
    cnt = 0
    temp_arr = []
    while cur <= n and idx < len(arr):
        if arr[idx] == cur:
            cur += 1
            idx += 1
        else:
            if cnt == k:
                temp_arr.sort()
                arr += temp_arr
                temp_arr = []
                ans += 1
                cnt = 0
            cnt += 1
            temp_arr.append(arr[idx])
            del arr[idx]
    if cnt > 0:
        ans += 1
    print(ans)
            
