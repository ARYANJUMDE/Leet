# Last updated: 12/27/2025, 6:56:18 PM
class Solution(object):
    def minimumSum(self, num):
        y=[]
        x=[]
        num=str(num)
        for num1 in num:
            x.append(int(num1))
        x.sort()
        for num2 in x:
            y.append(str(num2))
        z=int(y[0]+y[3])
        t=int(y[1]+y[2])
        
        return(z+t)