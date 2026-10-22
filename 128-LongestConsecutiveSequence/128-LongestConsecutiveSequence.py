# Last updated: 10/22/2026, 11:11:16 PM
1class Solution(object):
2    def longestConsecutive(self, nums):
3        if len(nums)==0:
4            return 0
5        if len(nums)==1:
6            return 1
7        nums.sort()
8        right=0
9        left=0
10        max_len=float('-inf')
11        curr_len=1
12        while right<len(nums)-1:
13            if nums[right+1]==nums[right]+1:
14                curr_len=curr_len+1
15            elif nums[right+1]==nums[right]:
16                pass
17            else:
18                while left!=right+1:
19                    left=left+1
20                    curr_len=curr_len-1
21                curr_len=1
22            if curr_len>max_len:
23                max_len=curr_len
24            right=right+1
25            
26        return(max_len)
27
28        