# Last updated: 9/26/2026, 6:56:40 PM
class Solution(object):
    def getMaximumConsecutive(self, coins):
        m = len(coins)
        coins.sort()
        maxreach=0
        i=0
        count=1
        for coin in coins:
            if i<m and coin<=maxreach+1:
                maxreach+=coin
                count+=1
            else:
                break
        
        return maxreach+1