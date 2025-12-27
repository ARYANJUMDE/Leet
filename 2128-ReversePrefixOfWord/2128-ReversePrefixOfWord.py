# Last updated: 12/27/2025, 6:56:21 PM
class Solution(object):
    def reversePrefix(self, word, ch):
        x=[]
        t=""
        for char in word:
            x.append(char)
        if ch in x:
            p=x.index(ch)
            for i in range(p+1):
                t=t+x[i]
        else:
            return(word)
        
        n=t[::-1]
        for j in range(p+1,len(x)):
            n=n+x[j]
        
        return(n)

        