# Last updated: 10/18/2026, 9:00:33 PM
1class Solution(object):
2    def minCostClimbingStairs(self, cost):
3        def climb(t,dp):
4            if t<=1:
5                return 0
6            if dp[t]!=-1:
7                return dp[t]
8            dp[t]= min(climb(t-1,dp)+cost[t-1],climb(t-2,dp)+cost[t-2])
9            return dp[t]
10        o=climb(len(cost),[-1]*(len(cost)+1))
11        return(o)
12
13        