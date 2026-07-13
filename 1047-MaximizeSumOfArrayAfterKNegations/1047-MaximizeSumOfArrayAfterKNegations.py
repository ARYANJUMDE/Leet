# Last updated: 7/13/2026, 10:09:06 PM
class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        for i in range(k):
            t=min(nums)
            nums.remove(t)
            t=t*-1
            nums.append(t)
        return(sum(nums))
        