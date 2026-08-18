# Last updated: 8/18/2026, 10:34:57 PM
1class Solution(object):
2    def findSubsequences(self, nums):
3        result=[]
4        def solve(a,i):
5            if i==len(nums):
6                if len(a)>=2 and a==sorted(a,reverse=False) and a not in result  :
7                    result.append(a[:])
8                    return
9            else:
10                a.append(nums[i])
11                solve(a,i+1)
12                a.pop()
13                solve(a,i+1)
14        solve([],0)
15        return result