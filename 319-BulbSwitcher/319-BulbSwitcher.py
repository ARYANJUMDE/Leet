# Last updated: 12/27/2025, 6:57:37 PM
import math
class Solution(object):
    def bulbSwitch(self, n):
        if(n==0):
            return 0
        else:
            return(int(math.ceil(-1+(n+1)**0.5)))


        