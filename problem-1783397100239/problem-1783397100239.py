# Last updated: 7/7/2026, 9:35:00 AM
1class Solution(object):
2    def sumAndMultiply(self, n):
3        if n==0:
4            return 0
5        s=str(n)
6        t=""
7        p=0
8        for ch in s:
9            if ch!="0":
10                t=t+ch
11                p=p+int(ch)
12        
13        
14        return(int(t)*p)
15
16        