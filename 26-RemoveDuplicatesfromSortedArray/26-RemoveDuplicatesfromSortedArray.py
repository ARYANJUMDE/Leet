# Last updated: 6/27/2026, 8:19:33 PM
1class Solution(object):
2    def runningSum(self, nums):
3        x=[]
4        for i in range(len(nums)):
5            x.append(sum(nums[:i+1]))
6        return(x)
7        # runningsum=[]
8        # t=0
9        # for i in range(len(nums)):
10        #     t=t+nums[i]
11        #     runningsum.append(t)
12        
13        # return(runningsum)
14        