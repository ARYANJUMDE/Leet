# Last updated: 2/27/2026, 11:30:39 AM
1class Solution(object):
2    def merge(self, nums1, m, nums2, n):
3        nums1[m:]=nums2[:n]
4        nums1.sort()
5        return(nums1)
6
7        