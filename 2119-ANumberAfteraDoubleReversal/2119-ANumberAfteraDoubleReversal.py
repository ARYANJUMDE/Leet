# Last updated: 2/15/2026, 10:44:40 AM
1class Solution(object):
2    def isSameAfterReversals(self, num):
3        x=str(num)
4        x=x[::-1]
5        y=int(x)
6        z=str(y)
7        z=z[::-1]
8        r=int(z)
9        if(r==num):
10            return(True)
11        else:
12            return(False)
13        