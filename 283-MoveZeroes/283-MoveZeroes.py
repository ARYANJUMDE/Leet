# Last updated: 12/27/2025, 6:57:40 PM
class Solution(object):
    def moveZeroes(self, nums):
        for num in nums:
            if(num==0):
                x=num
                nums.remove(num)
                nums.append(x)
                
        return(nums)  
        