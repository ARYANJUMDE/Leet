# Last updated: 12/27/2025, 6:56:08 PM
class Solution(object):
    def triangleType(self, nums):
        if not(nums[0]+nums[1]>nums[2] and nums[1]+nums[2]>nums[0] and nums[0]+nums[2]>nums[1]):
            return "none"
        if(nums[0]==nums[1]==nums[2]):
            return ("equilateral")
        elif(nums[0]==nums[1] or nums[0]==nums[2] or nums[1]==nums[2]):
            return ("isosceles")
        else:
            return ("scalene")
        