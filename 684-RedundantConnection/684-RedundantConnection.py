# Last updated: 4/13/2026, 5:54:46 PM
1from collections import deque
2
3class Solution(object):
4    def shortestPathBinaryMatrix(self, grid):
5        n = len(grid)
6        
7    
8        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
9            return -1
10        
11        
12        directions = [(-1,-1), (-1,0), (-1,1),
13                      (0,-1),        (0,1),
14                      (1,-1), (1,0), (1,1)]
15        
16        q = deque([(0, 0, 1)])  
17        grid[0][0] = 1  
18        
19        while q:
20            r, c, dist = q.popleft()
21            
22        
23            if r == n-1 and c == n-1:
24                return dist
25            
26            for dr, dc in directions:
27                nr, nc = r + dr, c + dc
28                
29                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
30                    q.append((nr, nc, dist + 1))
31                    grid[nr][nc] = 1 
32        
33        return -1