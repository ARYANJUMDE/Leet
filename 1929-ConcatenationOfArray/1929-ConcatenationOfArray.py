# Last updated: 9/9/2026, 10:11:58 PM
class Solution(object):
    def getConcatenation(self, nums):
        x=[]
        for num in nums:
            x.append(num)
        y=nums+x
        return(y)