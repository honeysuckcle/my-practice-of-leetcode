# Date: 2021/9/1
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        m, n = len(version1), len(version2)
        i, j = 0, 0
        while i<m or j<n:
            x, y  = 0, 0
            while i<m and version1[i] != '.':
                x = x*10 + ord(version1[i]) - ord('0')
                """
                上面这一行我也尝试过用int(version[i])
                但是这样速度慢了许多
                """
                i += 1
            i += 1
            while j < n and version2[j] != '.':
                y = y*10 + int(version2[j])
                j += 1
            j += 1
            if x > y:
                return 1
            if x < y:
                return -1
        return 0