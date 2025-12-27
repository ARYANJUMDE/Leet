# Last updated: 12/27/2025, 6:56:29 PM
class Solution(object):
    def maxProduct(self, nums):
        x=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                x.append((nums[i]-1)*(nums[j]-1))
        
        
        return(max(x))
        