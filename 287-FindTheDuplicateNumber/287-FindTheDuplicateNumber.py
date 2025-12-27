# Last updated: 12/27/2025, 6:57:39 PM
class Solution(object):
    def findDuplicate(self, nums):
        n=set()
        x=set()
        for num in nums:
            if num in n:
                x.add(num)
            else:
                n.add(num)
        for p in x:
            return(p)


        