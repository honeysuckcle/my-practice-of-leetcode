from re import M
s, m = input().split()
m = int(m)
ans = len(s)
if len(s) == 0:
    print(0)
else:
    p = abs(ord(s[0]) - ord('A'))
    i = 1
    mov = 0
    if m < len(s)-1 and m > 0:
        for j in range(1, m+1):
            mov += abs(ord(s[j]) - ord(s[j-1]))
        while i < len(s):
            if m <= mov:
                ans += m
                i += m
                if i+m < len(s):
                    m = 0
                    for j in range(1, m+1):
                        mov += abs(ord(s[j]) - ord(s[j-1]))
                else:
                    break
            else:
                ans += abs(ord(s[i]) - ord(s[i-1]))
                mov -= abs(ord(s[i]) - ord(s[i-1]))
                i += 1
                if i + m < len(s):
                    mov += abs(ord(s[i+m]) - ord(s[i+m-1]))
                else:
                    break
            
    for k in range(i, len(s)):
        ans += abs(ord(s[k]) - ord(s[k-1]))
    print(ans)