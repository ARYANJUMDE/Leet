# Last updated: 3/29/2026, 11:34:11 AM
1class Solution(object):
2    def createTargetArray(self, nums, index):
3        target=[]
4        for i in range(len(nums)):
5            target.insert(index[i],nums[i])
6        return(target)
7        