# Last updated: 7/19/2026, 4:43:44 PM
1class Solution(object):
2    def removeDuplicates(self, nums):
3        t=list(set(nums))
4        for i in range(len(t)):
5            if nums.count(t[i])>2:
6                for j in range(nums.count(t[i])-2):
7                    nums.remove(t[i])
8        return(len(nums))