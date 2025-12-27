# Last updated: 12/27/2025, 6:57:56 PM
class Solution(object):
    def findPeakElement(self, nums):
        max=nums[0]
        index=0
        for i in range(0,len(nums)-1):
            if(nums[i+1]>nums[i]):
                max=nums[i+1]
                index=i+1
        return(index)
        