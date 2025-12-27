# Last updated: 12/27/2025, 6:56:35 PM
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

        