# Last updated: 2/25/2026, 12:37:45 PM
1class Solution(object):
2    def generateParenthesis(self, n):
3        res = [] 
4        def backtrack(curr, open_count, close_count):  
5            if len(curr) == 2 * n:
6                res.append(curr)
7                return
8            if open_count < n:
9                backtrack(curr + "(", open_count + 1, close_count)
10            if close_count < open_count:
11                backtrack(curr + ")", open_count, close_count + 1)
12
13
14        backtrack("", 0, 0)
15        return res        