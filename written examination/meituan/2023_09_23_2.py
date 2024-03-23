hh, mm = list(map(int, input().split(':')))

n = int(input())
for i in range(n):
    ch, x = input().split()
    x = int(x)
    if ch == '+':
        new_mm = (mm+x) % 60
        hh = ((mm+x) // 60 + hh) % 24
        mm = new_mm
    elif ch == '-':
        new_mm = (mm-x) % 60
        hh = (hh + (mm-x) // 60) % 24
        mm = new_mm

if len(str(hh)) == 1:
    hh = '0' + str(hh)
if len(str(mm)) == 1:
    mm = '0' + str(mm)
print(str(hh) + ':' + str(mm))