# Last updated: 9/9/2026, 10:16:43 PM
class Solution(object):
    def dominantIndex(self, nums):
        x=max(nums)
        y=nums.index(x)
        nums.remove(x)
        count=0
        
        for i in range(len(nums)):
            if(x>(2*nums[i]) or x==(2*nums[i])):
                count=count+1
        if(count==len(nums)):
            return(y)
        
        else:
            return-1
        