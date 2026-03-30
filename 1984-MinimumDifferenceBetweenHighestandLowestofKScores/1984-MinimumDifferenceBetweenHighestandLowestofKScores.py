# Last updated: 3/30/2026, 9:50:22 AM
1from itertools import combinations
2class Solution(object):
3    def minimumDifference(self, nums, k):
4        # x=[]
5        # y=[]
6        # x.extend(combinations(nums,k))            
7        # for i in range(len(x)):
8        #     y.append(max(x[i])-min(x[i]))
9        # return(min(y))
10        nums.sort()
11        # x=[]
12        # y=[]
13        
14        # for i in range(k):
15        #     x.append(nums[i])
16        # nums.sort(reverse=True)
17        
18        # for i in range(k):
19        #     y.append(nums[i])
20        # t=max(x)-min(x)
21        # p=max(y)-min(y)
22        # return(min(t,p))
23        min_diff=float('inf')
24        for i in range(len(nums)-k+1):
25            diff=nums[i+k-1]-nums[i]
26            min_diff=min(min_diff,diff)
27        return min_diff
28        
29