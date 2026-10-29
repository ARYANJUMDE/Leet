# Last updated: 10/29/2026, 11:40:06 AM
1class Solution(object):
2    def destCity(self, paths):
3        x=set()
4        for i in range(len(paths)):
5            if paths[i][1] not in x:
6                x.add(paths[i][1])
7        for i in range(len(paths)):
8            if paths[i][0] in x:
9                x.remove(paths[i][0])
10        x=list(x)
11        return x[0]
12