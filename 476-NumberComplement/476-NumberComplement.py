# Last updated: 9/6/2026, 5:31:50 PM
1class Solution(object):
2    def findComplement(self, num):
3        z=bin(num)[2:]
4        p=""
5        for i in range(len(z)):
6            if z[i] =="0":
7                p=p+"1"
8            else:
9                p=p+"0"
10        return int(p,2)
11        