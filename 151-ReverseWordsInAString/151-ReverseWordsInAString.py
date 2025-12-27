# Last updated: 12/27/2025, 6:58:00 PM
class Solution(object):
    def reverseWords(self, s):
        x=s.split()
        x.reverse()
        t=""
        for i in range(len(x)):
            t=t+x[i]
            if i != len(x) - 1:
                t += " "
        
        return(t)
        