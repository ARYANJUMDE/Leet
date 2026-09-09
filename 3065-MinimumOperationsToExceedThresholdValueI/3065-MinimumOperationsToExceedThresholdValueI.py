# Last updated: 9/9/2026, 10:09:24 PM
class Solution(object):
    def minOperations(self, nums, k):
        count=0
        for num in nums:
            if num<k:
                count=count+1
        
        
        return(count)
        