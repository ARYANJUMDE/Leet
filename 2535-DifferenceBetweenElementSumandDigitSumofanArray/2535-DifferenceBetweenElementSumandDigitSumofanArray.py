# Last updated: 4/24/2026, 10:53:48 AM
1class Solution(object):
2    def differenceOfSum(self, nums):
3        t=sum(nums)
4        y=0
5        for i in range(len(nums)):
6            while nums[i]>0:
7                x=nums[i]%10
8                y=y+x
9                nums[i]=nums[i]//10
10        
11        
12        return(abs(t-y))
13        