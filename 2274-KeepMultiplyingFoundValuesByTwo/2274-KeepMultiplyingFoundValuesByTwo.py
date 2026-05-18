# Last updated: 5/18/2026, 12:44:05 PM
class Solution(object):
    def findFinalValue(self, nums, original):
        while original in nums:
            original=original*2
        return(original)

        