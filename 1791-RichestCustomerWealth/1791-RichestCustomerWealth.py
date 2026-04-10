# Last updated: 4/10/2026, 4:10:24 PM
class Solution(object):
    def maximumWealth(self, accounts):
        t=[]
        for i in range(len(accounts)):
            t.append(sum(accounts[i]))
        return(max(t))
        