# Last updated: 10/17/2026, 3:42:05 PM
1class Solution(object):
2     def twoSum(self, nums, target):
3#         for i in range(0,len(nums)-1):
4#             for j in range(i+1,len(nums)):
5#                 if(nums[i]+nums[j]==target):
6#                     return [i,j]
7# S=Solution()
8# S.twoSum([2,7,11,15],9)
9            # for i in range(len(nums)-1):
10            #     for j in range(i+1,len(nums)):
11            #         if nums[i]+nums[j]==target:
12            #             return([i,j])
13
14            t={}
15            for i in range(len(nums)):
16                if i not in t:
17                    t[i]=nums[i]
18            for i in (t):
19                diff=target-t[i]
20                for j in range(i+1,len(t)):
21                    if t[j]==diff:
22                        return([i,j])
23    
24
25