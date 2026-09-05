# Last updated: 9/5/2026, 4:24:07 PM
1class Solution(object):
2    def firstStableIndex(self, nums, k):
3        min1=[0]*len(nums)
4        min1[-1]=nums[-1]
5        for i in range(len(nums)-2,-1,-1):
6            min1[i]=min(nums[i],min1[i+1])
7        max1=nums[0]
8        for i in range(len(nums)):
9            if max1<nums[i]:
10                max1=nums[i]
11            if max1-min1[i]<=k:
12                return(i)
13        return -1
14        
15