# Last updated: 9/25/2026, 2:53:42 PM
1class Solution(object):
2    def makeIntegerBeautiful(self, n, target):
3        t=n
4        sum2=0
5        while t>0:
6            sum2=sum2+t%10
7            t=t//10
8        if sum2<=target:
9            return 0
10        if n==target:
11            return 0
12        p=str(n)
13        x=[]
14        for i in range(len(p)):
15            x.append(int(p[i]))
16        sum1=sum(x)
17        for i in range(len(x)-1,-1,-1):
18            diff=10-x[i]
19            sum1=sum1-x[i]
20            x[i]=0
21            if i==0:
22                x.insert(0,1)  
23            else:
24                x[i-1]=x[i-1]+1
25                j=i-1
26                while j>0 and x[j]==10:
27                    x[j]=0
28                    x[j-1]=x[j-1]+1
29                    j=j-1
30            sum1=sum(x)
31            if sum1<=target:
32                return(int("".join(map(str,x))))-n
33    
34    
35
36        