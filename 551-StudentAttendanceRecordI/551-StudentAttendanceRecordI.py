# Last updated: 4/9/2026, 10:02:33 AM
1class Solution(object):
2    def checkRecord(self, s):
3        if(s.count('A')<2 and s.count('LLL')==0):
4            return(True)
5        else:
6            return(False)
7        