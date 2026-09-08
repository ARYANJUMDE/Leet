# Last updated: 9/8/2026, 6:06:19 PM
1class Solution(object):
2    def countCommas(self, n):
3        x=str(n)
4        if len(x)<4:
5            return 0
6        else:
7            return n-1000+1
8        