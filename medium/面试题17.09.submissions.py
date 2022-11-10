class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        arr = [1]
        p1, p2, p3 = 0, 0, 0
        while len(arr) < k:
            arr.append(min(arr[p1]*3, arr[p2]*5, arr[p3]*7))
            if arr[-1] == arr[p1]*3:
                p1 += 1
            elif arr[-1] == arr[p2]*5:
                p2 += 1
            elif arr[-1] == arr[p3] * 7:
                p3 += 1
        return arr[k-1]
s = Solution()
print(s.getKthMagicNumber(7))