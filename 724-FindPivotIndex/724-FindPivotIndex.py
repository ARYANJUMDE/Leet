# Last updated: 12/27/2025, 6:56:56 PM
class Solution(object):
    def pivotIndex(self, nums):
        x=-1
        for i in range(0,len(nums)):
            if(sum(nums[0:i])==sum(nums[i+1:len(nums)+1])):
                x=i
                break
        if(x!=-1):
            return(x)
        else:
            return(-1)

        