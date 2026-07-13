# Last updated: 7/13/2026, 10:08:07 PM
class Solution(object):
    def canBeEqual(self, target, arr):
        if (sorted(arr)==sorted(target)):
            return(True)
        else:
            return(False)

        