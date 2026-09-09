# Last updated: 9/9/2026, 10:13:48 PM
class Solution(object):
    def createTargetArray(self, nums, index):
        target=[]
        for i in range(len(nums)):
            target.insert(index[i],nums[i])
        return(target)
        