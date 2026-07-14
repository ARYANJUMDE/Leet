# Last updated: 7/14/2026, 5:50:40 PM
1class Solution(object):
2    def arraySign(self, nums):
3        x=1
4        for i in range(len(nums)):
5            x=x*nums[i]
6        return self.signFunc(x)
7    def signFunc(self,x):
8        if x==0:
9            return 0
10        if x>0:
11            return 1
12        return -1
13
14        