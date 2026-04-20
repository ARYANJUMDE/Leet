# Last updated: 4/20/2026, 10:12:41 AM
1class Solution(object):
2    def maxDistance(self, colors):
3        x=[]
4        for i in range(len(colors)):
5            for j in range(i+1,len(colors)):
6                if colors[i]!=colors[j]:
7                    x.append(abs(i-j))
8        return(max(x))
9        