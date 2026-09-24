# Last updated: 9/24/2026, 2:39:39 PM
1class Solution(object):
2    def smallestIndex(self, nums):
3        for i in range(len(nums)):
4            sum1=0
5            while nums[i]>0:
6                sum1=sum1+nums[i]%10
7                nums[i]=nums[i]//10
8            if sum1==i:
9                return i
10        return -1
11