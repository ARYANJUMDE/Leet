# Last updated: 4/10/2026, 4:10:20 PM
class Solution(object):
    def getConcatenation(self, nums):
        x=[]
        for num in nums:
            x.append(num)
        y=nums+x
        return(y)