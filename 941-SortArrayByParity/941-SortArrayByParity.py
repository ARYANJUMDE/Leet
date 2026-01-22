# Last updated: 1/22/2026, 11:43:20 AM
class Solution(object):
    def sortArrayByParity(self, nums):
        x=[]
        y=[]
        for num in nums:
            if num%2==0:
                x.append(num)
            else:
               y.append(num) 
        return x+y
        