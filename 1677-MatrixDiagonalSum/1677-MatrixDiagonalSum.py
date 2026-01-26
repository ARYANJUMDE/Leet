# Last updated: 1/26/2026, 11:26:58 AM
class Solution(object):
    def diagonalSum(self, mat):
        x=[]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if(i==j):
                    x.append(mat[i][j])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if(i+j==len(mat)-1 and i!=j):
                    x.append(mat[i][j])
        return(sum(x))

        