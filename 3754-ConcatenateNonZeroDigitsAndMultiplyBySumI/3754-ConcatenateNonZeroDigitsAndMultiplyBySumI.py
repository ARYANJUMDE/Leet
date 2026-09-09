# Last updated: 9/9/2026, 10:08:40 PM
class Solution(object):
    def sumAndMultiply(self, n):
        if n==0:
            return 0
        s=str(n)
        t=""
        p=0
        for ch in s:
            if ch!="0":
                t=t+ch
                p=p+int(ch)
        
        
        return(int(t)*p)

        