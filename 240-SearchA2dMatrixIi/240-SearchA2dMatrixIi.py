# Last updated: 3/11/2026, 5:26:03 PM
class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            mini=0
            maxi=len(matrix[i])-1
            while maxi>=mini:
                mid=(maxi+mini)//2
                if(matrix[i][mid]==target):
                    return(True)
                elif(matrix[i][mid]>target):
                    maxi=mid-1

                else:
                    mini=mid+1
        else:
            return(False)
