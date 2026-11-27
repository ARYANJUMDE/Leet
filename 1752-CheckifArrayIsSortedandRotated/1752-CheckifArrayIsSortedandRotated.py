# Last updated: 11/27/2026, 9:16:23 PM
1class Solution:
2    def check(self, nums: list[int]) -> bool:
3        if nums==sorted(nums):
4            return True
5        else:
6            t=len(nums)
7            for i in range(t):
8                x=nums.pop(0)
9                nums.append(x)
10                if nums==sorted(nums):
11                    return True
12        return False
13        