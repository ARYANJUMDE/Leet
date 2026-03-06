# Last updated: 3/6/2026, 4:52:29 PM
1class Solution(object):
2    def checkOnesSegment(self, s):
3        x=[]
4        y=[]
5        for i in range(len(s)):
6            if s[i]=='1':
7                x.append(i)
8            else:
9                y.append(i)
10        for num in y:
11            if num+1 in x:
12                return(False)
13                
14        else:
15            return(True) 
16
17
18                    
19
20        