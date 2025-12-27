# Last updated: 12/27/2025, 6:57:41 PM
class Solution(object):
    def missingNumber(self, nums):
        for i in range(0,len(nums)+1):
            if i not in nums:
                return i
        