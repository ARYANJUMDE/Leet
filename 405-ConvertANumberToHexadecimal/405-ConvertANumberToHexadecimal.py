# Last updated: 12/27/2025, 6:57:19 PM
class Solution(object):
    def toHex(self, num):
        if num==0:
            return "0"
        return hex(num &0xFFFFFFFF)[2:]
        