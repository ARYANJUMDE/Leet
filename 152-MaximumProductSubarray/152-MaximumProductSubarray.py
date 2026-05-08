# Last updated: 5/8/2026, 1:08:58 PM
1import math
2class Solution(object):
3    def maxProduct(self, nums):
4        #x=[]
5        maxi=nums[0]
6        mini=nums[0]
7        ans=nums[0]
8
9        for i in range(1,len(nums)):
10            temp=maxi
11            maxi=max(nums[i],maxi*nums[i],mini*nums[i])
12            mini=min(nums[i],temp*nums[i],mini*nums[i])
13
14            ans=max(ans,maxi)
15
16        return(ans)
17
18
19        