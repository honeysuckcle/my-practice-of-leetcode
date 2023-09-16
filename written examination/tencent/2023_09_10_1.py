n, m = list(map(int, input().split()))
s = input()
ss = set(s)
c = input()
alpha = [0] * 26
ans = 0
for i, x in enumerate(c):
    if x in ss:
        if alpha[ord(x)-ord('a')] == 1:
            break
        alpha[ord(x)-ord('a')] = 1
        ans += 1
print(ans)