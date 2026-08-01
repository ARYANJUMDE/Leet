# Last updated: 8/1/2026, 2:03:51 PM
1class Solution(object):
2    def maxProductDifference(self, nums):
3        nums.sort()
4        return(nums[-1]*nums[-2]-nums[0]*nums[1])