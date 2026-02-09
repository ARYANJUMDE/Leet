# Last updated: 2/9/2026, 10:17:12 AM
class Solution(object):
    def isThree(self, n):
        count=0
        for i in range(1,n+1):
            if(n%i==0):
                count=count+1
        if(count==3):
            return(True)
        else:
            return False
        