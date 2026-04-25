# Last updated: 4/25/2026, 10:43:05 PM
1class Solution(object):
2    def canJump(self, nums):
3        reach=0
4        #This stores the farthest index you can reach so far
5        #Initially, you're at index 0, so reach = 0
6        for i in range(len(nums)):
7            #If current index i is greater than what you can reach,
8            #it means:
9            #you can’t even get to this position
10            if i>reach:
11                return(False)
12            else:
13                reach=max(reach,i+nums[i])
14        else:
15            return(True)