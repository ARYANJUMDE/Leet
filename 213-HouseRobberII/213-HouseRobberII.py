# Last updated: 5/31/2026, 10:52:50 AM
1class Solution(object):
2    def hammingWeight(self, n):
3        s=bin(n)
4        return s.count('1')
5        