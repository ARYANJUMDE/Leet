# Last updated: 2/27/2026, 11:25:17 AM
1class Solution(object):
2    def searchMatrix(self, matrix, target):
3        for i in range(len(matrix)):
4            mini=0
5            maxi=len(matrix[i])-1
6            while maxi>=mini:
7                mid=(maxi+mini)//2
8                if(matrix[i][mid]==target):
9                    return(True)
10                elif(matrix[i][mid]>target):
11                    maxi=mid-1
12
13                else:
14                    mini=mid+1
15        else:
16            return(False)
17