# Last updated: 6/25/2026, 9:37:45 PM
1class Solution(object):
2    def uniqueOccurrences(self, arr):
3        x=list(set(arr))
4        y=[]
5        for i in range(len(x)):
6            y.append(arr.count(x[i]))
7        if len(set(y))==len(y):
8            return(True)
9        else:
10            return(False)
11        