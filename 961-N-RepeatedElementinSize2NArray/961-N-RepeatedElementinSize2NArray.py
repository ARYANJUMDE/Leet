# Last updated: 2/25/2026, 11:57:10 AM
1class Solution(object):
2    def repeatedNTimes(self, nums):
3        x=[]
4        for num in nums:
5            if num not in x:
6                x.append(num)
7        for num in x:
8            if 2*nums.count(num)==len(nums):
9                return(num)
10    
11
12        