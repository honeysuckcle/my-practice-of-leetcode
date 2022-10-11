import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    ai = list(map(int, line.split()))
    res = 0
    gbs = 1
    def zxgbs(a, b):
        i = 2
        inshu = set()
        while i <= min(a,b):
            if a % i == 0 and b % i == 0:
                a /= i
                b /= i
                inshu.add(i)
            else:
                i += 1
        res = 1
        for i in list(inshu):
            res *= i
        return a*b*res
#     print(ai)
    for a in ai:
        if gbs % a != 0:
            gbs = zxgbs(gbs, a)
    for a in ai:
        if a % gbs == 0:
            res += 1
        
    print(res)