# Last updated: 10/1/2026, 9:35:52 PM
1class Solution(object):
2    def maxProfit(self, prices):
3        x=[]
4        for i in range(len(prices)-1):
5            if prices[i+1]-prices[i]>0:
6                x.append(prices[i+1]-prices[i])
7        if len(x)>0:
8            return sum(x)
9        return 0