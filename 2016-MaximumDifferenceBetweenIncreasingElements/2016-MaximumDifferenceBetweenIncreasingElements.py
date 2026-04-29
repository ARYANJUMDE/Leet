# Last updated: 4/29/2026, 11:21:02 AM
1class Solution(object):
2    def maximumDifference(self, nums):
3        x=[]
4        for i in range(len(nums)-1):
5            for j in range(i+1,len(nums)):
6                if(nums[i]<nums[j]):
7                    x.append(nums[j]-nums[i])
8        if(len(x)==0):
9            return(-1)
10        else:
11            return(max(x))
12        