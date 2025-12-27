# Last updated: 12/27/2025, 6:58:32 PM
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1=nums1+nums2
        nums1.sort()
        if(len(nums1)%2!=0):
            y=(float(nums1[int((len(nums1)-1)/2)]))
            return y
        else:
            x=float(nums1[int((len(nums1)-1)/2)]+nums1[int(((len(nums1)-1)+1)/2)])/2
            return x
S=Solution()
S.findMedianSortedArrays([1,3],[2])
        