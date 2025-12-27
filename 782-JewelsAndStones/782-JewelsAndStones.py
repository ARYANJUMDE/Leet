# Last updated: 12/27/2025, 6:56:53 PM
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count=0
        for ch in stones:
            if(ch in jewels):
                count=count+1
        
        
        return(count)
        