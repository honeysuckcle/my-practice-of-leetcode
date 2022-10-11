class Solution:
    def longestNiceSubarray(self, nums) -> int:
        res = 1
        l, r = 0, 1
        n = nums[0]
        while r < len(nums):
            if r-l == 0 or nums[r] & n == 0:
                r += 1
                len_ = r - l
                if res < len_:
                    res = len_
                n |= nums[r-1]
            else:
                n ^= nums[l] 
                l += 1
        return res

s = Solution()
print(s.longestNiceSubarray([1,3,8,48,10]))