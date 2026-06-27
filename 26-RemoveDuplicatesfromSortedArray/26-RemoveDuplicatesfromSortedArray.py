# Last updated: 6/27/2026, 10:33:28 PM
1class Solution(object):
2    def pivotIndex(self, nums):
3        # x=-1
4        # for i in range(0,len(nums)):
5        #     if(sum(nums[0:i])==sum(nums[i+1:len(nums)+1])):
6        #         x=i
7        #         break
8        # if(x!=-1):
9        #     return(x)
10        # else:
11        #     return(-1)
12        for i in range(len(nums)):
13            if sum(nums[:i])==sum(nums[i+1:]):
14                return(i)
15        else:
16            return(-1)
17    
18
19        