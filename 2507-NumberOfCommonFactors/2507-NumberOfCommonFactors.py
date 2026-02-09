# Last updated: 2/9/2026, 10:17:05 AM
class Solution(object):
    def commonFactors(self, a, b):
        z=min(a,b)
        count=0
        for i in range(1,z+1):
            if a%i==0 and b%i==0:
                count=count+1
        return(count)
        