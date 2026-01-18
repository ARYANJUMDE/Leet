# Last updated: 1/18/2026, 11:02:15 AM
1class Solution(object):
2    def sortArrayByParity(self, nums):
3        x=[]
4        y=[]
5        for num in nums:
6            if num%2==0:
7                x.append(num)
8            else:
9               y.append(num) 
10        return x+y
11        