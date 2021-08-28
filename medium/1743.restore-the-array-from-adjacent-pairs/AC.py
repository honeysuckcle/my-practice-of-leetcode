from collections import defaultdict

def restoreArray(adjacentPairs):
    m = n = len(adjacentPairs)
    n += 1
    cnts = defaultdict(int)
    hashmap = defaultdict(list)
    for a, b in adjacentPairs:
        cnts[a] += 1
        cnts[b] += 1
        hashmap[a].append(b)
        hashmap[b].append(a)
    start = -1
    for i, v in cnts.items():
        if v == 1:
            start = i
            break
    ans = [0] * n
    ans[0] = start
    ans[1] = hashmap[start][0]
    for i in range(2, n):
        x = ans[i - 1]
        for j in hashmap[x]:
            if j != ans[i - 2]:
                ans[i] = j
    return ans

if __name__ == "__main__":
    print (restoreArray([[2,1],[3,4],[3,2]]))

# 作者：AC_OIer
# 链接：https://leetcode-cn.com/problems/restore-the-array-from-adjacent-pairs/solution/gong-shui-san-xie-yi-ti-shuang-jie-dan-x-elpx/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。