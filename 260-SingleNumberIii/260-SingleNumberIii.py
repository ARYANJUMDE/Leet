# Last updated: 12/27/2025, 6:57:42 PM
class Solution(object):
    def singleNumber(self, nums):
        x=[]
        for num in nums:
            if(nums.count(num)==1):
                x.append(num)
                
        
        
        
        
        return(x)
        