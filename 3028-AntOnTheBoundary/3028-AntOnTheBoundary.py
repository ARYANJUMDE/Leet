# Last updated: 9/9/2026, 10:09:29 PM
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
        