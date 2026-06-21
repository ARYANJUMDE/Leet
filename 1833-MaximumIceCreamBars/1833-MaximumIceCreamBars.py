# Last updated: 6/21/2026, 12:08:56 PM
1class Solution(object):
2    def maxIceCream(self, costs, coins):
3        costs.sort()
4        count=0
5        for i in range(len(costs)):
6            if costs[i]<=coins:
7                count=count+1
8                coins=coins-costs[i]
9            else:
10                break   
11        return(count)
12
13        