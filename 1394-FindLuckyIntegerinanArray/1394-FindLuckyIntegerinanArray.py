# Last updated: 3/31/2026, 10:53:49 AM
1class Solution(object):
2    def findLucky(self, arr):
3        x=[]
4        y=[]
5        for num in arr:
6            if num not in x:
7                x.append(num)
8        for num in x:
9            if num==arr.count(num):
10                y.append(num)
11        if(len(y)==0):
12            return(-1)
13        
14        else:
15            return(max(y))
16
17        