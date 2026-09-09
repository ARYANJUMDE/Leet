# Last updated: 9/9/2026, 10:10:14 PM
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
        