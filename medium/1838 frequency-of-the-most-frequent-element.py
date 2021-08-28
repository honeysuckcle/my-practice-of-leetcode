"""
Date: 2021/7/19

"""
def maxFrequency(nums, k: int) -> int:
    nums.sort()
    print(nums)
    left = 0 # 较小数的最后一个
    right = 0 # 较大数的最后一个 
    length = len(nums)
    for i in range(length):
        if nums[i] > nums[0]:
            left = i - 1
            right = i
            break
    while right + 1 < length and nums[right + 1] == nums[right]:
        right += 1
    dis = nums[right] - nums[left]
    need = dis * (left + 1)

    
    while need <= k:
        k -= need
        left = right
        right = left + 1
        while right + 1 < length and nums[right + 1] == nums[right]:
            right += 1
        print(left, right)
        if left == length -1:
            return length
        
        dis = nums[right] - nums[left]
        need = dis * (left + 1)
        
    return right

print(maxFrequency([1,2,4], 5))
print(maxFrequency([3,9,6], 2))
print(maxFrequency([3,6,6], 3))