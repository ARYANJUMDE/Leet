# Last updated: 5/18/2026, 11:02:26 AM
1class Solution(object):
2    def maximizeSum(self, nums, k):
3        s=0
4        for i in range(k):
5            s=s+max(nums)
6            t=max(nums)
7            nums.append(max(nums)+1)
8            nums.remove(t)
9        return(s)
10
11        