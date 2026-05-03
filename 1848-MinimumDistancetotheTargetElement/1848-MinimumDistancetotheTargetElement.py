# Last updated: 5/3/2026, 10:55:49 AM
1class Solution(object):
2    def getMinDistance(self, nums, target, start):
3        t=[]
4        for i in range(len(nums)):
5            if nums[i]==target:
6                t.append(i)
7        x=[]
8        for i in range(len(t)):
9            x.append(abs(t[i]-start))
10        return(min(x))
11        