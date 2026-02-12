# Last updated: 2/12/2026, 9:46:57 AM
1class Solution(object):
2    def maximumCount(self, nums):
3        count1=0
4        count2=0
5        for i in range(len(nums)):
6            if(nums[i]>0):
7                count1=count1+1
8            elif(nums[i]<0):
9                count2=count2+1
10                
11        
12        return(max(count1,count2))
13        