# Last updated: 2/8/2026, 9:59:39 AM
1class Solution(object):
2    def commonFactors(self, a, b):
3        z=min(a,b)
4        count=0
5        for i in range(1,z+1):
6            if a%i==0 and b%i==0:
7                count=count+1
8        return(count)
9        