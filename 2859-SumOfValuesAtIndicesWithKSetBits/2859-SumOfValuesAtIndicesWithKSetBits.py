# Last updated: 9/9/2026, 10:09:43 PM
class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        x=0
        for i in range(0,len(nums)):
            y=bin(i)
            z=y[2:]
            if(z.count('1')==k):
                x=x+nums[i]
        return(x)

        