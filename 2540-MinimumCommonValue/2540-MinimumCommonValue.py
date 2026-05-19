# Last updated: 5/19/2026, 11:51:28 AM
1class Solution(object):
2    def getCommon(self, nums1, nums2):
3        nums2=set(nums2)
4        for num in nums1:
5            if num in nums2:
6                return(num)
7        return -1
8
9
10        