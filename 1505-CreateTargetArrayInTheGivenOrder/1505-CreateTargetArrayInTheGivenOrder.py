# Last updated: 3/29/2026, 11:37:39 AM
class Solution(object):
    def createTargetArray(self, nums, index):
        target=[]
        for i in range(len(nums)):
            target.insert(index[i],nums[i])
        return(target)
        