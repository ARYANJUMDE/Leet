# Last updated: 11/26/2026, 1:10:01 PM
1class Solution:
2    def canAliceWin(self, n: int) -> bool:
3        if n<10:
4            return False
5        else:
6            i=10
7            count=0
8            while n>=i:
9                n=n-i
10                i=i-1
11                count=count+1
12            if count%2!=0:
13                return True
14            return False
15
16        
17        