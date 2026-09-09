# Last updated: 9/9/2026, 10:14:12 PM
class Solution(object):
    def maximum69Number (self, num):
        st=str(num)
        x=[]
        for s in st:
            x.append(int(s))
        for i in range(len(x)):
            if(x[i]==6):
                x[i]=9
                break
        t=""
        for i in range(len(x)):
            
            t=t+str(x[i])
        return(int(t))

        