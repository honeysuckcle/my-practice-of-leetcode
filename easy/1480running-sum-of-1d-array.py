def runningSum(self, nums):
        res = []
        for i in range(len(nums)):
            if i >= 1:
                res.append(res[i-1] + nums[i])
            else:
                res.append(nums[i])
        return res