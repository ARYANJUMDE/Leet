# Last updated: 1/19/2026, 9:31:07 AM
1class Solution(object):
2    def countNegatives(self, grid):
3        count=0
4        for i in range(len(grid)):
5            for j in range(len(grid[0])):
6                if grid[i][j]<0:
7                    count=count+1
8        
9        return(count)
10        