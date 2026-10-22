# Last updated: 10/22/2026, 11:07:14 PM
1class Solution(object):
2    def longestConsecutive(self, nums):
3        if len(nums)==0:
4            return 0
5        if len(nums)==1:
6            return 1
7        nums.sort()
8        right=0
9        max_len=float('-inf')
10        curr_len=1
11        while right<len(nums)-1:
12            if nums[right+1]==nums[right]+1:
13                curr_len=curr_len+1
14            elif nums[right+1]==nums[right]:
15                pass
16            else:
17                curr_len=1
18            if curr_len>max_len:
19                max_len=curr_len
20            right=right+1
21            
22        return(max_len)
23
24        