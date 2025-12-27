# Last updated: 12/27/2025, 6:57:33 PM
class Solution(object):
    def isPowerOfFour(self, n):
        if n<=0:
            return False
        while n%4==0:
            n=n//4
        return n==1
        