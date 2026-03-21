# Last updated: 3/21/2026, 1:01:23 PM
1class Solution(object):
2    def addedInteger(self, nums1, nums2):
3        """
4        :type nums1: List[int]
5        :type nums2: List[int]
6        :rtype: int
7        """
8        nums1.sort(reverse=True)
9        nums2.sort(reverse=True)
10        x=nums2[0]-nums1[0]
11        return(x)
12
13        