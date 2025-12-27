# Last updated: 12/27/2025, 6:57:36 PM
class Solution(object):
    def isPowerOfThree(self, n):
        if n<=0:
            return False
        while n % 3==0:
            n=n//3
        return n==1
S=Solution()
S.isPowerOfThree(27)

        