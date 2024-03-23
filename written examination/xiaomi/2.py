s = input()
xiao = []
mi = []
n = len(s)
xiao_s = 'xiao'
mi_s = 'mi'
cnt_xiao = 0
cnt_mi = 0
for i in range(n):
    if i+4<=n and s[i:i+4] == 'xiao':
        xiao.append(i)
    if i+2 <= n and s[i:i+2] == 'mi':
        mi.append(i)
i, j = 0, 0
ans = 0
while i < len(xiao) and j < len(mi):
    if xiao[i] > mi[j]:
        ans += i
        j += 1
    else:
        i += 1
while j < len(mi):
    ans += len(xiao)
    j += 1
print(ans)