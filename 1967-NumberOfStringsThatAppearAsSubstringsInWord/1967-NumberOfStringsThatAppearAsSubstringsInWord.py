# Last updated: 9/9/2026, 10:11:54 PM
class Solution(object):
    def numOfStrings(self, patterns, word):
        count=0
        for ch in patterns:
            if ch in word:
                count=count+1
        
        
        return(count)
        