# Last updated: 6/27/2026, 5:56:51 PM
1class Solution(object):
2    def removeDuplicates(self, nums):
3        # i=0
4        # while i<len(nums):
5        #     j=i+1
6        #     while j<len(nums):
7        #         if nums[i]==nums[j]:
8        #             nums.pop(j)
9        #         else:
10        #             j=j+1
11        #     i=i+1
12        # return len(nums)
13        
14        x=list(set(nums))
15        for i in range(len(x)):
16            if nums.count(x[i])>1:
17                while nums.count(x[i])>1:
18                    nums.remove(x[i])
19        return(len(nums))   
20
21
22
23
24        
25
26
27
28