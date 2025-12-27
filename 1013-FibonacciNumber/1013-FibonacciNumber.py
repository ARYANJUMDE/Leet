# Last updated: 12/27/2025, 6:56:47 PM
class Solution(object):
    def fib(self, n):
        if(n==0 or n==1):
            return n
        l=[0,1]
        for i in range(2,n):
            l.append(l[i-1]+l[i-2])
        
        return l[len(l)-1]+l[len(l)-2]



S=Solution()
S.fib(2)
        
        