# Last updated: 4/10/2026, 4:09:58 PM
class Solution(object):
    def firstUniqueEven(self, nums):
        for i in range(len(nums)):
            if(nums.count(nums[i])==1 and nums[i]%2==0):
                return(nums[i])
        return -1
        

        