# Last updated: 5/13/2026, 3:38:22 PM
1class Solution(object):
2    def sumZero(self, n):
3        if n==1:
4            return([0])
5        else:
6            x=[]
7            if n%2==0:
8                for i in range(1,(n/2)+1):
9                    x.append(i)
10                for j in range(1,(n/2)+1):
11                    x.append(-j)
12            else:
13                
14                for i in range(0,(n//2)+1):
15                    x.append(i)
16                for j in range(1,(n//2)+1):
17                    
18                    x.append(-j)
19                
20                
21        return(x)
22        
23
24        