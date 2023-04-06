def isshunzi(a):
    if len(set(a)) == len(a) and max(a) - min(a) == len(a) - 1:
        return True
    return False
n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
l = 1
pre_isshunzi = isshunzi(arr[0:k])
ans = 1 if pre_isshunzi else 0
pre_min = min(arr[0:k])
pre_max = max(arr[0:k])
while l +k <= n:
    if pre_isshunzi:
        if arr[l-1] == arr[l+k-1]:
            ans += 1
        elif arr[l-1] == pre_min and arr[l+k-1] == pre_max+1:
            pre_max += 1
            pre_min += 1
            ans += 1
        elif arr[l-1] == pre_max and arr[l+k-1] == pre_min - 1:
            pre_max -= 1
            pre_max -= 1
            ans += 1
        else:
            pre_isshunzi = False
    elif isshunzi(arr[l:l+k]):
        ans += 1
        pre_isshunzi = True
        pre_min = min(arr[l:l+k])
        pre_max = max(arr[l:l+k])
    l += 1
print(ans)