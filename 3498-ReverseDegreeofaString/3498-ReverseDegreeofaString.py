# Last updated: 2/5/2026, 10:48:54 AM
1class Solution(object):
2    def reverseDegree(self, s):
3        x=[]
4        y=[]
5        z=[]
6        for i in range(26,0,-1):
7            x.append(i)
8        for ch in range(97,123):
9            y.append(chr(ch))
10        cost=0
11        for i in range(len(x)):
12            z.append((y[i],x[i]))
13        
14        for i in range(len(s)):
15            for j in range(len(z)):
16                if s[i]==z[j][0]:
17                    
18                    cost=cost+(i+1)*z[j][1]
19
20        
21        return(cost)
22
23        