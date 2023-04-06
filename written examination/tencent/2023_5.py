def calculete_point(b1, b2):
    y = (b1+b2)/2
    return y - b1, y
def outbox(x,y, h, w):
    if x > 0 and x < w and y > 0 and y < h:
        return False
    return True
h, w = list(map(int, input().split()))
m = int(input())
lines = {1:set(), -1:set()}
for _ in range(m):
    x1, y1, x2, y2 = list(map(int, input().split()))
    k = (y2-y1) // (x2-x1)
    lines[k].add(y1-k*x1)
if len(lines[1]) == 0 or len(lines[-1]) == 0:
    print(max(len(lines[1]), len(lines[-1]))+1)
else:
    ans = (len(lines[1])+1) *(len(lines[-1])+1)
    for b2 in lines[-1]:
        for b1 in lines[1]:
            x, y = calculete_point(b1, b2)
            if outbox(x, y, h, w):
                ans -= 1
    print(ans)