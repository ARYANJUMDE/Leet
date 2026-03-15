# Last updated: 3/15/2026, 11:11:35 AM
1class Solution(object):
2    def merge(self, intervals):
3        x=sorted(intervals,key=lambda t:t[0])
4        y=[x[0]]
5        for i in range(1,len(x)):
6            if(y[-1][1]>=x[i][0]):
7                y[-1][1]=max(y[-1][1],x[i][1])
8            else:
9                y.append(x[i])
10        
11        
12        return(y)
13
14
15        