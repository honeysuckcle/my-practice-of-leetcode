n = int(input())
x = 1
sum_arr = 0
len_x = 0
while len_x + x <= n:
    len_x += x
    sum_arr += (1+x) * x // 2
    x += 1
    sum_arr %= (1e9+7)
if n > len_x:
    sum_arr += (x+x-(n-len_x)+1) * (n-len_x) // 2
    sum_arr %= (1e9+7)
print(int(sum_arr))