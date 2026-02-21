# Last updated: 2/21/2026, 5:43:49 PM
1class Solution(object):
2    def solveNQueens(self, n):
3        res = []
4        board = [["."] * n for _ in range(n)]
5
6        cols = set()
7        diag1 = set() 
8        diag2 = set()  
9
10        def backtrack(r):
11            if r == n:
12                temp = ["".join(row) for row in board]
13                res.append(temp)
14                return
15            
16            for c in range(n):
17                if c in cols or (r - c) in diag1 or (r + c) in diag2:
18                    continue
19                
20                # place queen
21                board[r][c] = "Q"
22                cols.add(c)
23                diag1.add(r - c)
24                diag2.add(r + c)
25
26                backtrack(r + 1)
27                board[r][c] = "."
28                cols.remove(c)
29                diag1.remove(r - c)
30                diag2.remove(r + c)
31
32        backtrack(0)
33        return res
34        