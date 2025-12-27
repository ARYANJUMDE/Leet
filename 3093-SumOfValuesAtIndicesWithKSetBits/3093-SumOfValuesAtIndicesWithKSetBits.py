# Last updated: 12/27/2025, 6:56:13 PM
class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        x=0
        for i in range(0,len(nums)):
            y=bin(i)
            z=y[2:]
            if(z.count('1')==k):
                x=x+nums[i]
        return(x)

        