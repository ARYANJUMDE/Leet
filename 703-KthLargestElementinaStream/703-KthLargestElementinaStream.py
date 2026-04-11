# Last updated: 4/11/2026, 2:04:55 PM
1class Solution(object):
2    def eraseOverlapIntervals(self, intervals):
3        """
4        :type intervals: List[List[int]]
5        :rtype: int
6        """
7        if not intervals:
8            return 0
9
10        
11        intervals.sort(key=lambda x: x[1])
12
13        count = 0
14        prev_end = intervals[0][1]
15
16        for i in range(1, len(intervals)):
17            if intervals[i][0] >= prev_end:
18                
19                prev_end = intervals[i][1]
20            else:
21            
22                count += 1
23
24        return count