# Last updated: 9/9/2026, 10:12:54 PM
from collections import Counter

class Solution(object):
    def frequencySort(self, nums):
        count = Counter(nums)
        return sorted(nums, key=lambda x: (count[x], -x))

        