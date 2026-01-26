# Last updated: 1/26/2026, 11:26:48 AM
class Solution(object):
    def countDigits(self, num):
        x=[]
        r=str(num)
        for i in range((len(r))):
            x.append(int(r[i]))
        
        count=0
        for j in range(len(x)):
            if(num%x[j]==0):
                count=count+1
        return(count)
        