# Last updated: 1/30/2026, 3:49:14 PM
class Solution(object):
    def minOperations(self, nums, k):
        count=0
        for num in nums:
            if num<k:
                count=count+1
        
        
        return(count)
        