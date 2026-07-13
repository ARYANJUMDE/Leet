# Last updated: 7/13/2026, 10:11:36 PM
class Solution(object):
    def hammingWeight(self, n):
        s=bin(n)
        return s.count('1')
        