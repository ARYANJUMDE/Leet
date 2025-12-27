# Last updated: 12/27/2025, 6:58:14 PM
from itertools import permutations
class Solution(object):
    def permute(self, nums):
        x=[]
        t=permutations(nums,len(nums))
        for i in t:
            if i not in x:
                x.append(list(i))
        return(x)



        