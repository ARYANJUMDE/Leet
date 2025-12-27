# Last updated: 12/27/2025, 6:57:04 PM
class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort(reverse=True)
        x=[]
        i=0
        while i<len(nums):
            p,j=nums[i],nums[i+1]
            x.append(min(p,j))
            i=i+2
        return(sum(x))

        