# Last updated: 2/9/2026, 10:15:15 AM
1class Solution(object):
2    def isThree(self, n):
3        count=0
4        for i in range(1,n+1):
5            if(n%i==0):
6                count=count+1
7        if(count==3):
8            return(True)
9        else:
10            return False
11        