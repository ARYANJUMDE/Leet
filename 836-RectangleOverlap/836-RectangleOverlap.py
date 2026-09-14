# Last updated: 9/14/2026, 11:08:32 AM
1class Solution(object):
2    def isRectangleOverlap(self, rec1, rec2):
3        x_overlap=max(0,min(rec1[2],rec2[2])-max(rec1[0],rec2[0]))
4        y_overlap=max(0,min(rec1[3],rec2[3])-max(rec1[1],rec2[1]))
5        if(x_overlap*y_overlap>0):
6            return(True)
7        else:
8            return(False)
9
10        