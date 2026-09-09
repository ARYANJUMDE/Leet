# Last updated: 9/9/2026, 10:14:09 PM
class Solution(object):
    def sortByBits(self, arr):
        x=[]
        for i in range(0,len(arr)):
            y=bin(arr[i])
            z=y.count('1')
            x.append((arr[i],z))
        x=sorted(x, key=lambda t:(t[1],t[0]))
        result=[]
        for i in range(len(x)):
            result.append(x[i][0])
        return(result)