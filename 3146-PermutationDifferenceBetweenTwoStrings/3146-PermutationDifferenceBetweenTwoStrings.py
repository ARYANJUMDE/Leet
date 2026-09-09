# Last updated: 9/9/2026, 10:09:09 PM
class Solution(object):
    def findPermutationDifference(self, s, t):
        l=[]
        for i in range(len(s)):
            x=s[i]
            l.append(abs(s.index(s[i])-t.index(x)))
        
        
        return(sum(l))
        