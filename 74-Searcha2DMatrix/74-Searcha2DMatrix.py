# Last updated: 2/21/2026, 4:28:47 PM
1class Solution(object):
2    def searchMatrix(self, matrix, target):
3        for i in range(len(matrix)):
4            low=0
5            high=len(matrix[i])-1
6            while low<=high:
7                mid=(low+high)//2
8                if(matrix[i][mid]==target):
9                    return(True)
10                elif(matrix[i][mid]>target):
11                    high=mid-1
12                else:
13
14                    low=mid+1
15        else:
16             return(False)
17
18
19        