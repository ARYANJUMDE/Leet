# Last updated: 11/20/2026, 10:40:39 PM
1class Solution(object):
2    def groupThePeople(self, groupSizes):
3        x=list(set(groupSizes))
4        result=[]
5        for i in range(len(x)):
6            t=[]
7            for j in range(len(groupSizes)):
8                if groupSizes[j]==x[i]:
9                    t.append(j)
10            if len(t)==x[i]:
11                result.append(t)
12            else:
13                o=[]
14                for k in range(0,len(t)):
15                    if len(o)<x[i]:
16                        o.append(t[k])
17                    else:
18                        result.append(o)
19                        o=[]
20                        o.append(t[k])
21                if len(o)>0:
22                    result.append(o)
23        return result
24            
25        