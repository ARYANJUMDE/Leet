# Last updated: 9/9/2026, 10:14:04 PM
class Solution(object):
    def countNegatives(self, grid):
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]<0:
                    count=count+1
        
        return(count)
        