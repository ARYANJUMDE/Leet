# Last updated: 3/28/2026, 12:13:03 PM
1class Solution(object):
2    def judgeCircle(self, moves):
3        x=moves.count('U')
4        y=moves.count('D')
5        z=moves.count('L')
6        m=moves.count('R')
7        if(x==y and z==m):
8            return(True)
9        else:
10            return(False)
11
12        