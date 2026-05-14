# Last updated: 5/14/2026, 11:36:23 AM
1class Solution(object):
2    def isGood(self, nums):
3        z=max(nums)
4        if(nums.count(z)==2):
5            for i in range(1,z):
6                if i not in nums or nums.count(i)>1:
7                    return(False)
8            else:
9                return(True)
10        else:
11            return(False)
12    
13    
14