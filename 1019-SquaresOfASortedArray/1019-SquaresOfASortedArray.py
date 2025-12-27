# Last updated: 12/27/2025, 6:56:46 PM
class Solution(object):
    def sortedSquares(self, nums):
        x=[]
        for num in nums:
            x.append(num*num)
        x.sort()
        return x

        