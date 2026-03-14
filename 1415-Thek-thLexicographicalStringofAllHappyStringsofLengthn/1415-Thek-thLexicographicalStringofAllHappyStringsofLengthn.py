# Last updated: 3/14/2026, 11:00:13 AM
1class Solution(object):
2    def getHappyString(self, n, k):
3        from itertools import product
4        t=['a','b','c']
5        y=[]
6        for i in product(t,repeat=n):
7            t="".join(i)
8            count=0
9            for j in range(len(t)-1):
10                if(t[j]!=t[j+1]):
11                    count=count+1
12            if(count==len(t)-1):
13                y.append(t)
14        if(k>len(y)):
15            return("")
16        else:
17            
18            return(y[k-1])
19        