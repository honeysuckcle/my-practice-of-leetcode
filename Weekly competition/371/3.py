from typing import List
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        cnt1, cnt2 = 0, 0
        n = len(nums1)
        max1, max2 = min(nums1[-1], nums2[-1]), max(nums1[-1], nums2[-1])
        for i in range(n-1):
            p, q = nums1[i], nums2[i]
            if max(p, q) > max2 or min(p, q) > max1:
                return -1
            if p > max1:
                cnt1 += 1
            if q > max1:
                cnt2 += 1
        if nums1[-1] > nums2[-1]:
            cnt1 += 1
        else:
            cnt2 += 1
        return min(cnt2, cnt1)

        
s = Solution()
print(s.minOperations([9,12,2,4,13,1,8,17,14,11,15,14,8,18,1,20,20,6,14,10,1,10,9,3,20,19,18],
[12,16,3,8,4,19,18,11,13,12,9,9,3,2,2,12,17,7,14,18,2,8,19,6,8,16,20]))