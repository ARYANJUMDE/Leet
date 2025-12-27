# Last updated: 12/27/2025, 6:56:26 PM
from collections import Counter

class Solution(object):
    def frequencySort(self, nums):
        count = Counter(nums)
        return sorted(nums, key=lambda x: (count[x], -x))

        