# Last updated: 12/27/2025, 6:58:09 PM
class Solution(object):
    def addBinary(self, a, b):
        z=(bin(int(a,2)+int(b,2)))[2:] #(a,2)here 2 is base
        return z

        