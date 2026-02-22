# Last updated: 2/22/2026, 12:26:37 PM
1class Solution(object):
2    def countEven(self, num):
3        x=[]
4        y=[]
5        for i in range(1,num+1):
6            x.append(str(i))
7        for i in range(len(x)):
8            s=0
9            for j in range(len(x[i])):
10                s=s+int(x[i][j])
11            if(s%2==0):
12                y.append(s)
13        
14        return(len(y))
15
16    
17
18        