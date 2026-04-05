# Last updated: 4/5/2026, 12:23:34 PM
1class Solution(object):
2    def firstUniqueEven(self, nums):
3        for i in range(len(nums)):
4            if(nums.count(nums[i])==1 and nums[i]%2==0):
5                return(nums[i])
6        return -1
7        
8
9        