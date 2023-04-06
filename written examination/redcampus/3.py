# 需要用到线段树

n = input()
n = int(n)
arr = list(map(int, input().split()))
m = input()
m = int(m)
l_arr = list(map(int, input().split()))
r_arr = list(map(int, input().split()))
op_arr = input()
x_arr = list(map(int, input().split()))
for i in range(m):
    if op_arr[i] == '|':
        for j in range(l_arr[i]-1, r_arr[i]):
            arr[j] |= x_arr[i]
    elif op_arr[i] == '&':
        for j in range(l_arr[i]-1, r_arr[i]):
            arr[j] &= x_arr[i]
    elif op_arr[i] == '=':
        for j in range(l_arr[i]-1, r_arr[i]):
            arr[j] = x_arr[i]
print(arr)
        