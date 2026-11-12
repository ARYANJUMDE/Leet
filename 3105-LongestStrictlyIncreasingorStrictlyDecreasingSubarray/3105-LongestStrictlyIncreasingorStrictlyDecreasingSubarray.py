# Last updated: 11/12/2026, 12:50:01 PM
1class Solution:
2    def longestMonotonicSubarray(self, nums: List[int]) -> int:
3        if len(nums)==1:
4            return 1
5        maxlen1=float('-inf')
6        maxlen2=float('-inf')
7        i=0
8        j=0
9        currlen1=1
10        currlen2=1
11        while i<len(nums)-1:
12            if nums[i]<nums[i+1]:
13                currlen1=currlen1+1
14            else:
15                currlen1=1
16            if currlen1>maxlen1:
17                maxlen1=currlen1
18            i=i+1
19        
20        while j<len(nums)-1:
21            if nums[j]>nums[j+1]:
22                currlen2=currlen2+1
23            else:
24                currlen2=1
25            if currlen2>maxlen2:
26                maxlen2=currlen2
27            j=j+1
28        return max(maxlen1,maxlen2)
29        
30
31            
32
33
34
35
36
37        