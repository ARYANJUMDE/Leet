# Last updated: 7/10/2026, 3:25:26 PM
1class Solution(object):
2    def largestSumAfterKNegations(self, nums, k):
3        for i in range(k):
4            t=min(nums)
5            nums.remove(t)
6            t=t*-1
7            nums.append(t)
8        return(sum(nums))
9        