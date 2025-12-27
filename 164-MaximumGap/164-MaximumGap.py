# Last updated: 12/27/2025, 6:57:54 PM
class Solution(object):
    def maximumGap(self, nums):
        nums.sort()
        gp=0
        if(len(nums)==1):
            return(0)
        else:
            for i in range(len(nums)-1):
                if(nums[i+1]-nums[i]>gp):
                    gp=nums[i+1]-nums[i]
            return(gp)
        