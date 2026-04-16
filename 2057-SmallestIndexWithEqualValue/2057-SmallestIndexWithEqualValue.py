# Last updated: 4/16/2026, 11:44:28 AM
1class Solution(object):
2    def smallestEqual(self, nums):
3        for i in range(len(nums)):
4            if i%10==nums[i]:
5                return(i)
6        else:
7            return(-1)
8    
9        
10
11