# Last updated: 1/24/2026, 12:20:22 PM
1class Solution(object):
2    def diagonalSum(self, mat):
3        x=[]
4        for i in range(len(mat)):
5            for j in range(len(mat[0])):
6                if(i==j):
7                    x.append(mat[i][j])
8        for i in range(len(mat)):
9            for j in range(len(mat[0])):
10                if(i+j==len(mat)-1 and i!=j):
11                    x.append(mat[i][j])
12        return(sum(x))
13
14        