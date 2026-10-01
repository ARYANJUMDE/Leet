# Last updated: 10/1/2026, 6:30:50 PM
1class Solution(object):
2    def eraseOverlapIntervals(self, intervals):
3        # intervals.sort(key=lambda t:t[0])
4        # count=0
5        # for i in range(len(intervals)-1):
6        #     if intervals[i][1]>=intervals[i+1][1]:
7        #         count=count+1
8        
9        # return(count)
10        t=len(intervals)
11        intervals=sorted(intervals,key=lambda x:(x[0]))
12        for i in range(len(intervals)-1):
13            if intervals[i][0]==intervals[i+1][0] and intervals[i][1]>intervals[i+1][1]:
14                intervals[i],intervals[i+1]=intervals[i+1],intervals[i]
15        i=0
16        while i<len(intervals)-1:
17            if intervals[i+1][0]<intervals[i][1]:
18                if intervals[i][1]<=intervals[i+1][1]:
19                    intervals.pop(i+1)
20                else:
21                    intervals.pop(i)
22                i=i
23            else:
24                i=i+1
25        return t-len(intervals)
26