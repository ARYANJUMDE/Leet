# Last updated: 3/25/2026, 4:59:44 PM
1class Solution(object):
2    def wordPattern(self, pattern, s):
3        x=[]
4        y=[]
5        x=s.split()
6        t=[]
7        if len(pattern)!=len(x):
8            return False
9        for ch2 in x:
10            if ch2 not in t:
11                t.append(ch2)
12
13        for ch in pattern:
14            if ch not in y:
15                y.append(ch)
16        if(len(t)!=len(y)):
17
18            return False
19        for i in range(len(pattern)):
20            if(y.index(pattern[i])!=t.index(x[i])):
21                return False
22        return True
23
24        