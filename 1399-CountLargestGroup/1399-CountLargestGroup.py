# Last updated: 3/9/2026, 5:52:22 PM
1class Solution(object):
2    def countLargestGroup(self, n):
3        x=[]
4        for i in range(1,n+1):
5            s=0
6            t=str(i)
7            for ch in t:
8                s=s+int(ch)
9            x.append(s)
10        r=list(set(x))
11        y=x.count(x[0])
12        count=0
13
14        for num in r:
15            if x.count(num)>y:
16                y=x.count(num)
17        
18        for num in r:
19            if x.count(num)==y:
20                count=count+1
21        return(count)
22        