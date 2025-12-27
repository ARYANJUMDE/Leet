# Last updated: 12/27/2025, 6:56:58 PM
class Solution(object):
    def findMaxAverage(self, nums, k):
        # Step 1: calculate sum of first window
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Step 2: slide the window across nums
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]   # add new, remove old
            max_sum = max(max_sum, window_sum)

        # Step 3: return max average
        return float(max_sum) / k

        