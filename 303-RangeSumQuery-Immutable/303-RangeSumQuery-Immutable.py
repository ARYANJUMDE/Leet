# Last updated: 2/25/2026, 11:59:20 AM
1class NumArray(object):
2    def __init__(self, nums):
3        self.prefix = [0] * (len(nums) + 1)
4        for i in range(len(nums)):
5            self.prefix[i + 1] = self.prefix[i] + nums[i]
6
7    def sumRange(self, left, right):
8        return self.prefix[right + 1] - self.prefix[left]
9