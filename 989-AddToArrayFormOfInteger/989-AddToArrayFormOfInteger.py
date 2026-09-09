# Last updated: 9/9/2026, 10:15:40 PM
class Solution(object):
    def addToArrayForm(self, num, k):
        g=[]
        r=[]
        x=""
        for i in num:
            g.append(str(i))
        for t in g:
            x=x+t
        p=str(int(x)+k)
        for st in p:
            r.append(int(st))
        
        return(r)

        