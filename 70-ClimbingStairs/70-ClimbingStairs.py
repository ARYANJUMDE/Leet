# Last updated: 8/13/2026, 6:03:25 PM
1class Solution(object):
2    def climbStairs(self, n):
3        if n==1 or n==0:
4            return 1
5        dp=[-1]*(n+1)
6        dp[0]=1
7        dp[1]=1
8        for i in range(2,len(dp)):
9            dp[i]=dp[i-1]+dp[i-2]
10        return dp[n]
11        