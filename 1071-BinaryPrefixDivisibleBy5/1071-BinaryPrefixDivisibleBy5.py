# Last updated: 7/13/2026, 10:09:01 PM
class Solution(object):
    def prefixesDivBy5(self, nums):
        z=[]
        for i in range(len(nums)):
            z.append(str(nums[i]))
        x=[]
        t=z[0]
        answer=[]
        for j in range(1,len(z)+1):
            x.append(t+''.join(z[1:j]))
        for i in range(len(x)):
            if int(x[i],2)%5==0:
                answer.append(True)
            else:
                answer.append(False)
        return(answer)
        