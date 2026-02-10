# Last updated: 2/10/2026, 4:15:14 PM
1import math
2class Solution(object):
3    def findGCD(self, nums):
4        x=max(nums)
5        y=min(nums)
6        z=[]
7        p=[]
8        for i in range(1,x+1):
9            if(x%i==0):
10                z.append(i)
11        for j in range(1,y+1):
12            if(y%j==0):
13                p.append(j)
14        curr=z[0]
15        for i in range(1,len(z)):
16            if z[i] in p:
17                if curr<z[i]:
18                    curr=z[i]
19        return(curr)
20
21