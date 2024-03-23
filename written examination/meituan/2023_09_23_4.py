import collections
def get_yinzi(x):
    ans = collections.defaultdict(int)
    while x > 1:
        for i in range(2, x+1):
            if x % i == 0:
                ans[i] += 1
                x //= i
                break
    return ans

def is_wqpf(yinzi_i, x_yinzi):
    new_dict = collections.defaultdict(int)
    for k, v in yinzi_i.items():
        new_dict[k] += v
    for k, v in x_yinzi.items():
        new_dict[k] += v
    for v in new_dict.values():
        if v % 2 != 0:
            return False
    return True
n, q = list(map(int, input().split()))
arr = list(map(int, input().split()))
yinzi = [get_yinzi(x) for x in arr]
for _ in range(q):
    l, r, x = list(map(int, input().split()))
    x_yinzi = get_yinzi(x)
    flag = True
    for i in range(l, r+1):
        if not is_wqpf(yinzi[i], x_yinzi):
            print(arr[i])
            flag = False
            break
    if flag:
        print(-1)