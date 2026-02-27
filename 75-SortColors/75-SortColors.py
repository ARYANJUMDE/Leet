# Last updated: 2/27/2026, 11:41:18 AM
class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]>nums[j]):
                    nums[i],nums[j]=nums[j],nums[i]


        return(nums)
        