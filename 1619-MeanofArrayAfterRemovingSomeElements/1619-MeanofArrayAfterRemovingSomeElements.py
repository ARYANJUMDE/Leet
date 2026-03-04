# Last updated: 3/4/2026, 9:24:50 AM
1class Solution(object):
2    def trimMean(self, arr):
3        arr.sort()
4        k=int(len(arr)*0.05)
5        x=float(sum(arr[k:-k]))/len(arr[k:-k])
6        return x
7        