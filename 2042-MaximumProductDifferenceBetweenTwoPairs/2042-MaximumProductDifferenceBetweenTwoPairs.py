# Last updated: 8/19/2026, 4:15:43 PM
class Solution(object):
    def maxProductDifference(self, nums):
        nums.sort()
        return(nums[-1]*nums[-2]-nums[0]*nums[1])