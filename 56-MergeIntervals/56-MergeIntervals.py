# Last updated: 6/29/2026, 12:36:03 PM
1class Solution(object):
2    def insert(self, intervals, newInterval):
3        intervals.append(newInterval)
4        intervals=sorted(intervals,key=lambda x:x[0])
5        i=0
6        while i<len(intervals)-1:
7            if intervals[i][1]>=intervals[i+1][0]:
8                intervals.insert(i,[intervals[i][0],max(intervals[i+1][1],intervals[i][1])])
9                intervals.pop(i+1)
10                intervals.pop(i+1)
11                i=i-1
12            i=i+1
13        
14        return(intervals)
15