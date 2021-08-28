"""
Date: 2021/7/16
统计一个数字在排序数组中出现的次数。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2

面试官肯定是考二分才会出这道题

"""
def search(nums, target: int) -> int:
    count = 0
    for i in nums:
        if i == target:
            count += 1
    return count


if __name__ == "__main__":
    res = search([5,7,7,8,8,10], 8)
    print(res)
