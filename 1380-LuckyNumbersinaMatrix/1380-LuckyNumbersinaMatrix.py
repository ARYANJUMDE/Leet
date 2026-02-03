# Last updated: 2/3/2026, 4:05:56 PM
1class Solution(object):
2    def luckyNumbers(self, matrix):
3        row_min=[]
4        col_max=[]
5        for i in range(len(matrix)):
6            row_min.append(min(matrix[i]))
7        for j in range(len(matrix[0])):
8            max_val=matrix[0][j]
9            for i in range(len(matrix)):
10                if matrix[i][j]>max_val:
11                    max_val=matrix[i][j]
12            col_max.append(max_val)
13            
14        res=[]
15        for num in row_min:
16            if num in col_max:
17                
18                res.append(num)
19        return res
20        