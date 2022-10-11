from collections import defaultdict
from email.policy import default
# 超时

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        dict_ = defaultdict(int)
        for i in range(n):
            dict_[s[i]] += 1
        res = n
        cnt = list(dict_.values()).count(1)
        for x in range(n-2):
            if x != 0:
                dict_[s[x-1]] -= 1
                if dict_[s[x-1]] == 1:
                    cnt += 1
                if dict_[s[x-1]] == 0:
                    cnt -= 1
            sub_dict = dict_.copy()
            sub_cnt = cnt
            for y in range(n-2-x):
                if y != 0:
                    sub_dict[s[n-y]] -= 1
                    if sub_dict[s[n-y]] == 1:
                        sub_cnt += 1
                    if sub_dict[s[n-y]] == 0:
                        sub_cnt -= 1
                res += sub_cnt
        return res

s = Solution()
print(s.uniqueLetterString("ABC"))