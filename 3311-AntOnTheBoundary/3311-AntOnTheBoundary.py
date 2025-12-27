# Last updated: 12/27/2025, 6:56:06 PM
class Solution(object):
    def returnToBoundaryCount(self, nums):
        boundary=0
        sums=0
        count=0
        for i in range(len(nums)):
            sums=sums+nums[i]
            if(sums==boundary):
                count=count+1
        return(count)
        