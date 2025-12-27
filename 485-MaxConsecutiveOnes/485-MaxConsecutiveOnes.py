# Last updated: 12/27/2025, 6:57:11 PM
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        x=[]
        count=0
        for num in nums:
            if(num==1):
                count=count+1
            else:
                x.append(count)
                count=0
        x.append(count)
        return(max(x))

        