# Last updated: 12/27/2025, 6:58:06 PM
class Solution(object):
    def subsets(self, nums):
        from itertools import combinations
        t=[]
        for i in range(0,len(nums)+1):
            for com in combinations(nums,i):
                t.append(list(com))
        return (t)
        