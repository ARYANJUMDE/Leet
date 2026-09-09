# Last updated: 9/9/2026, 10:14:00 PM
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        x=[]
        for i in range(len(nums)):
            count=0
            max=nums[i]
            for j in range(len(nums)):
                if(nums[i]>nums[j]):
                    count=count+1
            x.append(count)
        
        return(x)

        