# Last updated: 5/22/2026, 10:59:37 AM
1class Solution(object):
2    def search(self, nums, target):
3        for i in range(len(nums)):
4            if nums[i]==target:
5                return i
6        return -1
7        