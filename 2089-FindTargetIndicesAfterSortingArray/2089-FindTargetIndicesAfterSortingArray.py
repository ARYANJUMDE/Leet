# Last updated: 2/1/2026, 12:41:39 PM
1class Solution(object):
2    def targetIndices(self, nums, target):
3        nums.sort()
4        x=[]
5        for i in range(len(nums)):
6            if nums[i]==target:
7                x.append(i)
8        return(x)
9        