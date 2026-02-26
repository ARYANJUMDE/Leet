# Last updated: 2/26/2026, 10:44:02 AM
1class Solution(object):
2    def combinationSum(self, candidates, target):
3        result=[]
4        def backtrack(start, path, total):
5            if total == target:
6                result.append(path[:])
7                return
8            if total > target:
9                return
10            for i in range(start, len(candidates)):
11                
12                path.append(candidates[i])
13                backtrack(i, path, total + candidates[i])
14                path.pop()
15        backtrack(0, [], 0)
16        return result
17        