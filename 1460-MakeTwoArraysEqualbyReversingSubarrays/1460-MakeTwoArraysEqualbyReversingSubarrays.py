# Last updated: 7/11/2026, 12:10:15 PM
1class Solution(object):
2    def canBeEqual(self, target, arr):
3        if (sorted(arr)==sorted(target)):
4            return(True)
5        else:
6            return(False)
7
8        