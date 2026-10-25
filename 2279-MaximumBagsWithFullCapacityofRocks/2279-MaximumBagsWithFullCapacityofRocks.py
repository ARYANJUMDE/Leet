# Last updated: 10/25/2026, 5:24:48 PM
1class Solution(object):
2    def maximumBags(self, capacity, rocks, additionalRocks):
3        x=[]
4        for i in range(len(capacity)):
5            t=capacity[i]-rocks[i]
6            if t!=0:
7                x.append(t)
8        x.sort()
9        count=len(capacity)-len(x)
10        for i in range(len(x)):
11            if additionalRocks>=x[i]:
12                additionalRocks=additionalRocks-x[i]
13                x[i]=0
14                count=count+1
15            else:
16                break
17        
18        return(count)
19