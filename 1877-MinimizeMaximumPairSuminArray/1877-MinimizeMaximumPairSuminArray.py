# Last updated: 11/15/2026, 12:03:10 PM
1class Solution(object):
2    def minPairSum(self, nums):
3        nums.sort()
4        max_sum=float('-inf')
5        for i in range(len(nums)//2):
6            curr_sum=nums[i]+nums[len(nums)-i-1]
7            if max_sum<curr_sum:
8                max_sum=curr_sum
9        return max_sum
10        