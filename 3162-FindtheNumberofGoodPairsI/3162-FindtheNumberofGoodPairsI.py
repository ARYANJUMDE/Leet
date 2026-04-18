# Last updated: 4/18/2026, 10:18:01 AM
1class Solution(object):
2    def numberOfPairs(self, nums1, nums2, k):
3        count=0
4        for i in range(len(nums1)):
5            for j in range(len(nums2)):
6                if nums1[i]%(nums2[j]*k)==0:
7                    count=count+1
8        return(count)
9        