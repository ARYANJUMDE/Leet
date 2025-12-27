# Last updated: 12/27/2025, 6:56:05 PM
class Solution(object):
    def findPermutationDifference(self, s, t):
        l=[]
        for i in range(len(s)):
            x=s[i]
            l.append(abs(s.index(s[i])-t.index(x)))
        
        
        return(sum(l))
        