# Last updated: 9/14/2026, 2:15:32 PM
1class Solution(object):
2    def numSubarraysWithSum(self, nums, goal):
3        count1=0
4        sum1=0
5        r=0
6        l=0
7        while r<len(nums):
8            sum1=sum1+nums[r]
9            if sum1>goal:
10                while sum1>goal:
11                    sum1=sum1-nums[l]
12                    l=l+1
13            count1=count1+(r-l+1)
14            r=r+1
15        sum1=0
16        count2=0
17        r=0
18        l=0
19        if goal==0:
20            return count1
21        while r<len(nums):
22            sum1=sum1+nums[r]
23            if sum1>goal-1:
24                while sum1>goal-1:
25                    sum1=sum1-nums[l]
26                    l=l+1
27            count2=count2+(r-l+1)
28            r=r+1
29        return abs(count2-count1)
30        
31        