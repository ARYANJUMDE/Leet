# Last updated: 8/20/2026, 6:22:46 PM
1from itertools import permutations
2class Solution(object):
3    def permute(self, nums):
4        result=[]
5        def solve(a,map1):
6            if len(a)==len(nums):
7                result.append(a[:])
8                return
9            else:
10                for i in range(len(nums)):
11                    if i not in map1:
12                        a.append(nums[i])
13                        map1.append(i)
14                        solve(a,map1)
15                        a.pop()
16                        map1.pop()
17        solve([],[])
18        return result
19
20
21
22        # x=[]
23        # t=permutations(nums,len(nums))
24        # for i in t:
25        #     if i not in x:
26        #         x.append(list(i))
27        # return(x)
28
29
30
31        