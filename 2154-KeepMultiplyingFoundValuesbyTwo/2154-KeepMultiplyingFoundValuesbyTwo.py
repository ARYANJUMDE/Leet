# Last updated: 4/30/2026, 10:39:42 AM
1class Solution(object):
2    def findFinalValue(self, nums, original):
3        while original in nums:
4            original=original*2
5        return(original)
6
7        