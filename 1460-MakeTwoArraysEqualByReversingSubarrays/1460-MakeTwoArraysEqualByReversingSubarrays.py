# Last updated: 9/9/2026, 10:13:27 PM
class Solution(object):
    def canBeEqual(self, target, arr):
        if (sorted(arr)==sorted(target)):
            return(True)
        else:
            return(False)

        