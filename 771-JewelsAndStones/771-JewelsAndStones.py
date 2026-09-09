# Last updated: 9/9/2026, 10:16:33 PM
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count=0
        for ch in stones:
            if(ch in jewels):
                count=count+1
        
        
        return(count)
        