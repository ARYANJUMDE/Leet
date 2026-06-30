# Last updated: 6/30/2026, 10:40:20 AM
1class Solution(object):
2    def leftRightDifference(self, nums):
3        t=[]
4        for i in range(len(nums)):
5            x=sum(nums[:i])
6            y=sum(nums[i+1:])
7            t.append(abs(x-y))
8        return(t)