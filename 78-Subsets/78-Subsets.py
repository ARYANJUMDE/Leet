# Last updated: 8/18/2026, 6:20:40 PM
1class Solution(object):
2    def subsets(self, nums):
3        result=[]
4        def solve(a,i):
5            if i==len(nums):
6                result.append(a[:])
7                return 
8            else:
9                a.append(nums[i])
10                solve(a,i+1)
11                a.pop()
12                solve(a,i+1)
13        solve([],0)
14        return result
15
16        
17
18        # from itertools import combinations
19        # t=[]
20        # for i in range(0,len(nums)+1):
21        #     for com in combinations(nums,i):
22        #         t.append(list(com))
23        # return (t)
24
25
26# len(nums) = length of the list. For [1,2,3], it’s 3.
27
28# range(len(nums)+1) = range(4) = [0, 1, 2, 3].
29
30# So r takes values: 0, 1, 2, 3.
31
32# Meaning: we will generate subsets of size 0, size 1, size 2, size 3.
33# combinations(nums, r) generates all subsets of length r.
34
35# Example:
36
37# If r = 0 → [()] (just the empty subset).
38
39# If r = 1 → [(1), (2), (3)].
40
41# If r = 2 → [(1,2), (1,3), (2,3)].
42
43# If r = 3 → [(1,2,3)].
44
45# combo is a tuple, e.g. (1,2).