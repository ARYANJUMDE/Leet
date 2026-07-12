# Last updated: 7/12/2026, 3:59:41 PM
1class Solution(object):
2    def countPairs(self, nums, target):
3        count=0
4        for i in range(0,len(nums)-1):
5            for j in range(i+1,len(nums)):
6                if nums[i]+nums[j]<target:
7                    count=count+1
8        return(count)
9
10        