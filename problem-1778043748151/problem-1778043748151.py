# Last updated: 5/6/2026, 10:32:28 AM
1class Solution(object):
2    def kthDistinct(self, arr, k):
3        x=[]
4        for ch in arr:
5            if arr.count(ch)==1:
6                x.append(ch)
7        if(len(x)<k):
8            return("")
9        else:
10            return(x[k-1])
11