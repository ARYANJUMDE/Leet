# Last updated: 7/13/2026, 10:11:27 PM
class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            prev1 = 0
            prev2 = 0

            for num in arr:
                temp = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = temp

            return prev1

        return max(
            helper(nums[:-1]),
            helper(nums[1:])
        )
    
