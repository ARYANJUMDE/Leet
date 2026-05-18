# Last updated: 5/18/2026, 12:44:12 PM
class Solution(object):
    def smallestEqual(self, nums):
        for i in range(len(nums)):
            if i%10==nums[i]:
                return(i)
        else:
            return(-1)
    
        

