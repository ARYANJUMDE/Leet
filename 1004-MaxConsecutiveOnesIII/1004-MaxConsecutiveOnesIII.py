# Last updated: 9/12/2026, 9:50:05 PM
1class Solution(object):
2    def longestOnes(self, nums, k):
3        # x=[]
4        # for i in range(len(nums)):
5        #     for j in range(i+1,len(nums)+1):
6        #         if nums[i:j].count(0)<=k:
7        #             x.append(len(nums[i:j]))
8        # if len(x)==0:
9        #     return 0
10        # return(max(x))
11        l=0
12        r=0
13        max_len=0
14        final_len=0
15        while r<len(nums):
16            if k>0:
17                max_len=max_len+1
18                if nums[r]==0:
19                    k=k-1
20            else:
21                if nums[r]==1:
22                    max_len=max_len+1
23                else:
24                    while k==0:
25                        if nums[l]==0:
26                            k=k+1
27                        l=l+1
28                        max_len=max_len-1
29                    max_len=max_len+1
30                    k=k-1
31            if max_len>final_len:
32                final_len=max_len
33            r=r+1
34        return final_len
35                
36                        
37                    