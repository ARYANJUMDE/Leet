# Last updated: 12/27/2025, 6:56:10 PM
import math
class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        x=[]
        k=[]
        for i in range(len(dimensions)):
            y=math.sqrt(dimensions[i][0]**2+dimensions[i][1]**2)
            z=dimensions[i][0]*dimensions[i][1]
            x.append((y,z))
            k.append((y,z))
        x=sorted(x,key=lambda t:(t[0],t[1]),reverse=True)
        k=sorted(k,key=lambda t:(t[1],t[0]),reverse=True)
        p=x[0][1]
        if(x.count(p)>1):
            return(k[0][1])
        else:
            return(p)

