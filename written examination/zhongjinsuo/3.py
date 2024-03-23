m, n, yymm, x = input().split(',')
yy = int(yymm[:2])
mm = int(yymm[2:])
m = int(m)
n = int(n)
x = int(x)
jiyue = [3,6,9,12]
lz = set()
for i in range(x):
    months = set()
    for j in range(m):
        months.add((yy + (mm+j) // 12, (mm+j) % 12))
    k = 0
    while k < len(jiyue) and jiyue[k] < mm:
        k += 1
    jiyue_y = yy
    for j in range(n):
        if k == len(jiyue):
            k = 0
            jiyue_y += 1
        while (jiyue_y , jiyue[k]) in months:
            k += 1
            if k == len(jiyue):
                k = 0
                jiyue_y += 1
        months.add((jiyue_y , jiyue[k]))
    new_months = list(months - lz)
    new_month_str = []
    for new_m in new_months:
        if len(str(new_m[1])) == 1:
            new_month_str.append('IZ'+str(new_m[0])+'0'+str(new_m[1]))
        else:
            new_month_str.append('IZ'+str(new_m[0])+str(new_m[1]))
    print(','.join(new_month_str))
    lz |= months
    mm += 1
    if mm == 12:
        yy += 1
        mm = 1