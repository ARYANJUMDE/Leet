# Last updated: 9/28/2026, 3:07:52 PM
1class Solution(object):
2    def minCuttingCost(self, n, m, k):
3        cost=0
4        if m<=k:
5            cost=0
6        else:
7            diff=m-k
8            cost=cost+diff*k
9        if n<=k:
10            cost=cost+0
11        else:
12            diff=n-k
13            cost=cost+diff*k
14        return(cost)