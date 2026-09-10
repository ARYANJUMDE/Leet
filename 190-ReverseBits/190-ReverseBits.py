# Last updated: 9/10/2026, 5:42:26 PM
1class Solution(object):
2    def reverseBits(self, n):
3        t=bin(n)[2:].zfill(32)
4        z=t[::-1]
5        return int(z,2)
6        