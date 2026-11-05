# Last updated: 11/5/2026, 10:19:52 AM
1class Solution(object):
2    def countPairs(self, nums, k):
3        count=0
4        for i in range(len(nums)):
5            for j in range(i+1,len(nums)):
6                if nums[i]==nums[j]:
7                    if i*j%k==0:
8                        count=count+1
9        return count
10        