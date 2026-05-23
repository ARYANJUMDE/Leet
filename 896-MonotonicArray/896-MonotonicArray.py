# Last updated: 5/23/2026, 10:55:32 AM
1class Solution(object):
2    def isMonotonic(self, nums):
3        if nums==sorted(nums):
4            return(True)
5        elif nums==sorted(nums,reverse=True):
6            return(True)
7        else:
8            return(False)
9
10        