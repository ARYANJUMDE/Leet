# Last updated: 10/16/2026, 1:38:47 PM
1class Solution:
2    def maxSubArray(self, nums: list[int]) -> int:
3        l=0
4        r=0
5        sum1=0
6        max_sum=float('-inf')
7        while r<len(nums):
8            sum1=sum1+nums[r]
9            if sum1<0:
10                while sum1<0:
11                    sum1=sum1-nums[l]
12                    l=l+1
13            if sum1>max_sum:
14                max_sum=sum1
15            r=r+1
16        if max_sum==0:
17            if 0 not in nums:
18                return max(nums)
19        return(max_sum)
20    
21        
22
23
24
25        