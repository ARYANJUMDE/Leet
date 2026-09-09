# Last updated: 9/9/2026, 10:11:02 PM
class Solution(object):
    def findFinalValue(self, nums, original):
        while original in nums:
            original=original*2
        return(original)

        