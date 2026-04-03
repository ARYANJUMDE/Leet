# Last updated: 4/3/2026, 4:31:03 PM
1class Solution(object):
2    def maximumWealth(self, accounts):
3        t=[]
4        for i in range(len(accounts)):
5            t.append(sum(accounts[i]))
6        return(max(t))
7        