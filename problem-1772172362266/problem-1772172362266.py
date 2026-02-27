# Last updated: 2/27/2026, 11:36:02 AM
1class Solution(object):
2    def sortColors(self, nums):
3        for i in range(len(nums)):
4            for j in range(i+1,len(nums)):
5                if(nums[i]>nums[j]):
6                    nums[i],nums[j]=nums[j],nums[i]
7
8
9        return(nums)
10        