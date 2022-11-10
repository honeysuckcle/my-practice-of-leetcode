from typing import List
def validPartition(nums: List[int]) -> bool:
    l = len(nums)
    if l == 2:
        if nums[0] == nums[1]:
            return True
        else:
            return False
    elif l == 3:
        if nums[0] == nums[1] and nums[1] == nums[2]:
            return True
        elif nums[1] - nums[0] == 1 and nums[2] - nums[1] == 1:
            return True
        else:
            return False
    elif l == 1:
        return False
    else:
        return (validPartition(nums[2:]) and validPartition(nums[:2])) or (validPartition(nums[3:]) and validPartition(nums[:3]))

print(validPartition([1,1,1,2]))


