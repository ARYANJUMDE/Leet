# Last updated: 9/17/2026, 6:47:17 PM
1class Solution(object):
2    def findSubarrays(self, nums):
3        r=0
4        s=[]
5        l=0
6        sum1=0
7        curr_len=0
8        while r<len(nums):
9            sum1=sum1+nums[r]
10            curr_len=curr_len+1
11            if curr_len>2:
12                while curr_len>2:
13                    sum1=sum1-nums[l]
14                    curr_len=curr_len-1
15                    l=l+1
16            if curr_len==2:
17                s.append(sum1)
18            r=r+1
19        if len(s)==len(set(s)):
20            return False
21        if len(s)>len(set(s)):
22            return True
23            
24
25        