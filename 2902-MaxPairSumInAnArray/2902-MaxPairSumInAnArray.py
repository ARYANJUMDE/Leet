# Last updated: 5/18/2026, 12:43:48 PM
class Solution(object):
    def maxSum(self, nums):
        x=[]
        for i in range(len(nums)):
            y=[]
            s=str(nums[i])
            for ch in s:
                y.append(int(ch))
            x.append(max(y))
        t=[]
        x=list(set(x))
        for i in range(len(x)):
            
            p=[]
            for j in range(len(nums)):
                if str(x[i])==max(str(nums[j])):
                    
                    p.append(nums[j])
            if len(p)>1:
                t.append(p)
        if(len(t)==0):
            return(-1)
        else:
            z=[]
            for i in range(len(t)):
                t[i].sort(reverse=True)
                z.append(t[i][0]+t[i][1])
            return(max(z))