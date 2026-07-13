# Last updated: 7/13/2026, 10:12:57 PM
class Solution(object):
    def search(self, nums, target):
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1
        