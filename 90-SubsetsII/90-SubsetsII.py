# Last updated: 8/18/2026, 6:56:09 PM
1class Solution(object):
2    def subsetsWithDup(self, nums):
3        result=[]
4        def solve(a,i):
5            if i==len(nums):
6                if sorted(a) not in result:
7                    result.append(sorted(a[:]))
8                return 
9            else:
10                a.append(nums[i])
11                solve(a,i+1)
12                a.pop()
13                solve(a,i+1)
14        solve([],0)
15        return (result)
16
17        # x=[[]]
18        # for i in range(len(nums)):
19        #     if [nums[i]] not in x:
20        #         x.append([nums[i]])
21        # for i in range(len(nums)-1):
22        #     t=[nums[i]]
23        #     for j in range(i+1,len(nums)):
24        #         t=t+[nums[j]]
25        #         if t not in x:
26        #             x.append(t)
27        
28        # return(x)
29