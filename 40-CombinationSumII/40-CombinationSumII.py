# Last updated: 10/11/2026, 11:23:51 AM
1class Solution(object):
2    def combinationSum2(self, candidates, target):
3        y=[]
4        def solve(x,i,sum1):
5            if i>len(candidates) or sum1>target:
6                return
7            if i==len(candidates):
8                if sum1==target:
9                    if sorted(x) not in y:
10                        y.append(sorted(x[:]))
11                return
12            x.append(candidates[i])
13            sum1=sum1+candidates[i]
14            solve(x,i+1,sum1)
15            sum1=sum1-candidates[i]
16            x.pop()
17            while i<len(candidates)-1 and candidates[i]==candidates[i+1]:
18                i=i+1
19            solve(x,i+1,sum1)
20        solve([],0,0)
21        return y
22        