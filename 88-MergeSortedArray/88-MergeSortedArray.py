# Last updated: 2/27/2026, 11:41:16 AM
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:]=nums2[:n]
        nums1.sort()
        return(nums1)

        