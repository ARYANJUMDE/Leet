# Last updated: 9/13/2026, 1:37:43 PM
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
11        # l=0
12        # r=0
13        # max_len=0
14        # final_len=0
15        # while r<len(nums):
16        #     if k>0:
17        #         max_len=max_len+1
18        #         if nums[r]==0:
19        #             k=k-1
20        #     else:
21        #         if nums[r]==1:
22        #             max_len=max_len+1
23        #         else:
24        #             while k==0:
25        #                 if nums[l]==0:
26        #                     k=k+1
27        #                 l=l+1
28        #                 max_len=max_len-1
29        #             max_len=max_len+1
30        #             k=k-1
31        #     if max_len>final_len:
32        #         final_len=max_len
33        #     r=r+1
34        # return final_len
35        r=0
36        l=0
37        curr_len=0
38        max_len=0
39        while r<len(nums):
40            if k>0:
41                curr_len=curr_len+1
42                if nums[r]==0:
43                    k=k-1
44            elif k==0 and nums[r]!=0:
45                curr_len=curr_len+1
46            elif k==0 and nums[r]==0:
47                curr_len=curr_len+1
48                while k==0:
49                    if nums[l]==0:
50                        k=k+1
51                    curr_len=curr_len-1
52                    l=l+1
53                k=k-1
54            if curr_len>max_len:
55                max_len=curr_len
56            r=r+1
57        return max_len
58
59                    