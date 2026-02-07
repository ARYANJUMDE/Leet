# Last updated: 2/7/2026, 11:44:17 AM
1class Solution(object):
2    def removeDuplicates(self, nums):
3        i=0
4        while i<len(nums):
5            j=i+1
6            while j<len(nums):
7                if nums[i]==nums[j]:
8                    nums.pop(j)
9                else:
10                    j=j+1
11            i=i+1
12        return len(nums)
13
14
15