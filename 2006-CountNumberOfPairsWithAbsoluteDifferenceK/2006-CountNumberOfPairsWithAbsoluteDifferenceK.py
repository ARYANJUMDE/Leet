# Last updated: 9/9/2026, 10:11:42 PM
class Solution(object):
    def countKDifference(self, nums, k):
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(abs(nums[i]-nums[j])==k):
                    count=count+1
        
        return(count)