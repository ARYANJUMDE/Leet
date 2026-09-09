# Last updated: 9/9/2026, 10:09:21 PM
class Solution(object):
    def addedInteger(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        nums1.sort(reverse=True)
        nums2.sort(reverse=True)
        x=nums2[0]-nums1[0]
        return(x)

        