# Last updated: 2/19/2026, 10:58:01 AM
1class Solution(object):
2    def runningSum(self, nums):
3        runningsum=[]
4        t=0
5        for i in range(len(nums)):
6            t=t+nums[i]
7            runningsum.append(t)
8        
9        return(runningsum)
10        