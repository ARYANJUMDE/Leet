# Last updated: 9/9/2026, 10:08:55 PM
class Solution(object):
    def findClosest(self, x, y, z):
        if(abs(z-x)<abs(z-y)):
            return 1
        elif(abs(z-y)<abs(z-x)):
            return 2
        else:
            return 0
        