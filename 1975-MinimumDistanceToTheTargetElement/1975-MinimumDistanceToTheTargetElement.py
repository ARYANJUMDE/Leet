# Last updated: 5/18/2026, 12:44:26 PM
class Solution(object):
    def getMinDistance(self, nums, target, start):
        t=[]
        for i in range(len(nums)):
            if nums[i]==target:
                t.append(i)
        x=[]
        for i in range(len(t)):
            x.append(abs(t[i]-start))
        return(min(x))
        