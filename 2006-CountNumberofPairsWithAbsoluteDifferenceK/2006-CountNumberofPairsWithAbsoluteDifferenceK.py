# Last updated: 4/6/2026, 8:52:54 PM
1class Solution(object):
2    def countKDifference(self, nums, k):
3        count=0
4        for i in range(len(nums)):
5            for j in range(i+1,len(nums)):
6                if(abs(nums[i]-nums[j])==k):
7                    count=count+1
8        
9        return(count)