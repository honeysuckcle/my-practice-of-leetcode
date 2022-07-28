def zeroFilledSubarray(nums) -> int:
        res = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if i == 0 or nums[i-1] != 0:
                    res += 1
                elif nums[i-1] == 0:
                    res += count + 1
                count += 1
            else:
                count == 0
        return res

zeroFilledSubarray([1,3,0,0,2,0,0,4])