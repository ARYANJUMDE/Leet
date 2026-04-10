# Last updated: 4/10/2026, 4:10:17 PM
class Solution(object):
    def countKDifference(self, nums, k):
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(abs(nums[i]-nums[j])==k):
                    count=count+1
        
        return(count)