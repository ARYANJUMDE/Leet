# Last updated: 12/27/2025, 6:57:52 PM
class Solution(object):
    def largestNumber(self, nums):
        x=[]
        for i in range(len(nums)):
            x.append(str(nums[i]))
        for j in range(len(x)):
            for k in range(j+1,len(x)):
                if(x[j]+x[k]<x[k]+x[j]):
                    x[j],x[k]=x[k],x[j]
        x=''.join(x)
        if(int(x)==0):
            return "0"
        return(x)

        