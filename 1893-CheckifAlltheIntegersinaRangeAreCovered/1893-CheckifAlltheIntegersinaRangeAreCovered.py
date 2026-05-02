# Last updated: 5/2/2026, 10:51:06 AM
1class Solution(object):
2    def isCovered(self, ranges, left, right):
3        x=[]
4        for i in range(len(ranges)):
5            for j in range(ranges[i][0],ranges[i][1]+1):
6                x.append(j)
7        for i in range(left,right+1):
8            if i not in x:
9                return(False)
10        else:
11            return(True)
12        