# Last updated: 11/1/2026, 10:47:34 AM
1class Solution(object):
2    def findMiddleIndex(self, nums):
3        for i in range(len(nums)):
4            if sum(nums[:i])==sum(nums[i+1:]):
5                return i
6        return -1