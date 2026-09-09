# Last updated: 9/9/2026, 10:13:19 PM
class Solution(object):
    def maxProduct(self, nums):
        x=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                x.append((nums[i]-1)*(nums[j]-1))
        
        
        return(max(x))
        