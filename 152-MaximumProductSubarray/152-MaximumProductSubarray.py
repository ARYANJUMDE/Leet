# Last updated: 10/20/2026, 1:01:03 PM
1import math
2class Solution(object):
3    def maxProduct(self, nums):
4        #x=[]
5        #maxi = maximum product till current index
6        #mini = minimum product till current index
7        #We keep minimum also because:negative × negative = positive
8        # maxi=nums[0]
9        # mini=nums[0]
10        # ans=nums[0]
11
12        # for i in range(1,len(nums)):
13
14        #     #Needed because maxi changes before calculating mini.
15        #     temp=maxi
16        #     #At every element, 3 possibilities:
17        #     #Start new subarray Extend previous maximum product or Extend previous minimum product
18        #     maxi=max(nums[i],maxi*nums[i],mini*nums[i])
19        #     mini=min(nums[i],temp*nums[i],mini*nums[i])
20
21        #     #Store global maximum.
22
23        #     ans=max(ans,maxi)
24
25        # return(ans)
26        max_prod=float('-inf')
27        prefix=1
28        suffix=1
29        for i in range(len(nums)):
30            prefix=prefix*nums[i]
31            suffix=suffix*nums[len(nums)-1-i]
32            if max_prod<prefix:
33                max_prod=prefix
34            if max_prod<suffix:
35                max_prod=suffix
36            if nums[i]==0:
37                prefix=1
38            if nums[len(nums)-i-1]==0:
39                suffix=1
40        if max_prod==float('-inf'):
41            return min(nums)
42        if max_prod<0 and 0 not in nums :
43            return(max_prod)
44        elif max_prod<0 and 0 in nums:
45            return(0)
46        else:
47            return(max_prod)
48    
49
50        