ans = ''
n = input()
n = int(n)
l, r = -90, 90
while r-l > 6:
    mid = (l+r) // 2
    if mid < n:
        l = mid + 1
        ans += '1'
    else:
        r = mid - 1
        ans += '0'
if mid < n:
    l = mid + 1
    ans += '1'
else:
    r = mid - 1
    ans += '0'
print(ans)