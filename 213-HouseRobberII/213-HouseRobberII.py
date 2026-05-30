# Last updated: 5/30/2026, 11:09:32 AM
1class Solution(object):
2    def rob(self, nums):
3        if len(nums) == 1:
4            return nums[0]
5
6        def helper(arr):
7            prev1 = 0
8            prev2 = 0
9
10            for num in arr:
11                temp = max(prev1, prev2 + num)
12                prev2 = prev1
13                prev1 = temp
14
15            return prev1
16
17        return max(
18            helper(nums[:-1]),
19            helper(nums[1:])
20        )
21    
22