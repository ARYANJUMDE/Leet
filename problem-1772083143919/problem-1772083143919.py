# Last updated: 2/26/2026, 10:49:03 AM
1class Solution(object):
2    def uniquePathsIII(self, grid):
3        m = len(grid)
4        n = len(grid[0])
5        empty = 0
6        for i in range(m):
7            for j in range(n):
8                if grid[i][j] != -1:
9                    empty += 1
10                if grid[i][j] == 1:
11                    sx, sy = i, j
12        self.ans = 0
13        
14        
15        def dfs(x, y, count):
16            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == -1:
17
18                return
19            if grid[x][y] == 2:
20                if count == empty:   
21                    self.ans += 1
22                return
23            temp = grid[x][y]
24            grid[x][y] = -1
25            
26            dfs(x+1, y, count+1)
27            dfs(x-1, y, count+1)
28            dfs(x, y+1, count+1)
29            dfs(x, y-1, count+1)
30            
31            
32            grid[x][y] = temp
33        
34    
35        dfs(sx, sy, 1)
36        return self.ans
37        