# Last updated: 9/9/2026, 10:13:08 PM
class Solution(object):
    def numIdenticalPairs(self, nums):
        count=0
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if(nums[i]==nums[j]):
                    count=count+1
                    
        return(count)
        