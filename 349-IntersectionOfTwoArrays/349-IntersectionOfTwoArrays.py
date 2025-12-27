# Last updated: 12/27/2025, 6:57:30 PM
class Solution(object):
    def intersection(self, nums1, nums2):
        num3=[]
        for num  in nums1:
            if num in nums2 and num not in num3:
                num3.append(num)
        return num3


S=Solution()
S.intersection([1,2,2,1],[2,2])
        