# Last updated: 3/10/2026, 4:05:52 PM
1class Solution(object):
2    def rob(self, nums):
3        prev1 = 0
4        prev2 = 0
5        
6        for num in nums:
7            temp = max(prev1, prev2 + num)
8            prev2 = prev1
9            prev1 = temp
10        
11        return prev1