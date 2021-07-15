# Date: 2021/7/15
# 无论数组中的数字是什么，最大值都不可能超过数组的长度，这是由第二个条件决定的；
# 但是如果数组中本身的元素就非常小，极端情况是全部都为1，那么可能的最大值也只能是1，
# 因为所有数组都只能变得更小，不能变得更大。
# 因此，解题思路为：
# 1. 找到数组中的最大值
# 2. 将最大值和数组长度作比较，如果超过数组长度，就把它变成数组长度
# 3. 直到数组最大值小于数组长度的时候，遍历一遍确保相邻元素差值
# 分析了半天，上述思路超时
# 查看评论发现。。。我想太多了，只需要对数组排序，之后完成第3步就好了


def maximumElementAfterDecrementingAndRearranging(arr) -> int:
    length = len(arr)
    print(arr)
    start = min(arr)
    if start > 1:
        arr.remove(start)
        arr.append(1)

    arr.sort()
    for i in range(1, length):
        if(arr[i] - arr[i-1] > 1):
            arr[i] = arr[i-1] + 1

    return max(arr)


if __name__ == "__main__":
    m = maximumElementAfterDecrementingAndRearranging([1,2,2,4,5,6])
    print(m)