# Last updated: 4/4/2026, 2:48:47 PM
1class Solution(object):
2    def getConcatenation(self, nums):
3        x=[]
4        for num in nums:
5            x.append(num)
6        y=nums+x
7        return(y)