# Last updated: 12/27/2025, 6:57:45 PM
class Solution(object):
    def isPowerOfTwo(self, n):
        # for i in range(0,n+1):
        #     if(2**i==n):
        #         return True
        #         break
        # else:
        #     return False
        if n<=0:
            return False
        while n%2==0:
            n=n//2
        return n==1