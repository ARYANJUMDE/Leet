# Last updated: 10/11/2026, 10:36:54 AM
1class Solution(object):
2    def sumOfSquares(self, nums):
3        sum1=0
4        x=len(nums)
5        for i in range(1,len(nums)+1):
6            if x%i==0:
7                sum1=sum1+nums[i-1]*nums[i-1]
8        return sum1
9
10        