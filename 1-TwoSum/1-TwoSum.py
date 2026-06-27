# Last updated: 6/27/2026, 5:25:31 PM
1class Solution(object):
2     def twoSum(self, nums, target):
3#         for i in range(0,len(nums)-1):
4#             for j in range(i+1,len(nums)):
5#                 if(nums[i]+nums[j]==target):
6#                     return [i,j]
7# S=Solution()
8# S.twoSum([2,7,11,15],9)
9            for i in range(len(nums)-1):
10                for j in range(i+1,len(nums)):
11                    if nums[i]+nums[j]==target:
12                        return([i,j])
13
14