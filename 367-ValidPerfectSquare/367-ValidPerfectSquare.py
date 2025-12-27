# Last updated: 12/27/2025, 6:57:28 PM
class Solution(object):
    def isPerfectSquare(self, num):
        for i in range(0,int(num**0.5)+1):
            if(i*i==num):
                return True
        else:
            return False
        