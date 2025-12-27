# Last updated: 12/27/2025, 6:56:55 PM
class Solution(object):
    def selfDividingNumbers(self, left, right):
        l=[]
        for i in range(left,right+1):
            x=i
            t=True
            while(x>0):
                rem=x%10
                if(rem==0 or i%rem!=0):
                    t=False
                    break
                x//=10
            if(t==True):
                l.append(i)
        return(l)

        