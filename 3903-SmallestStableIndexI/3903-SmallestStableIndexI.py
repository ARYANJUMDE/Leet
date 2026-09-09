# Last updated: 9/9/2026, 10:08:23 PM
class Solution(object):
    def firstStableIndex(self, nums, k):
        for i in range(len(nums)):
            t=max(nums[:i+1])
            v=min(nums[i:])
            if t-v<=k:
                return i
        return -1
        