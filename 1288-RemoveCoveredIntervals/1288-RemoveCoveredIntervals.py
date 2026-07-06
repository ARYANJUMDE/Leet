# Last updated: 7/6/2026, 1:25:13 PM
1class Solution(object):
2    def removeCoveredIntervals(self, intervals):
3        intervals=sorted(intervals,key=lambda x:(x[0],-x[1]))
4        i=0
5        while i<(len(intervals)-1):
6            if intervals[i][0]<=intervals[i+1][0] and intervals[i][1]>=intervals[i+1][1]:
7                intervals[i]=[intervals[i][0],intervals[i][1]]
8                intervals.pop(i+1)
9            else:
10                i=i+1
11        
12        return(len(intervals))
13
14