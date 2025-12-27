# Last updated: 12/27/2025, 6:58:07 PM
class Solution(object):
    def climbStairs(self, n):
        a=0
        b=1
        for i in range(0,n):
            a,b=b,a+b
            
        return (b)
        