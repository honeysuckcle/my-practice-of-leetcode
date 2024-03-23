class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        if a > b:
            temp = a
            a = b
            b = temp
        base = n-1
        mod = int(1e9+7)
        while base >= 0:
            bina, binb = (a >> base) & 1, (b >> base)&1
            if bina == binb:
                if bina == 0:
                    a += (1<<base)
                    b += (1<<base)
            else:
                if bina == 0:
                    tempa = a + (1<<base)
                    tempb = b - (1<<base)
                    if tempa < tempb:
                        a, b = tempa, tempb
                    
            base -= 1
        return ((a % mod) * (b % mod)) % mod
    
s = Solution()
print(s.maximumXorProduct(12, 5, 4))