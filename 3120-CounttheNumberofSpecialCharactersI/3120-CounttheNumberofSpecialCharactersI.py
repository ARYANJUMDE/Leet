# Last updated: 5/26/2026, 10:29:34 AM
1class Solution(object):
2    def numberOfSpecialChars(self, word):
3        x=[]
4        y=[]
5        count=0
6        for i in range(97,123):
7            x.append(chr(i))
8        for j in range(65,91):
9            y.append(chr(j))
10        s=""
11        z=[]
12        for ch in word:
13            if ch not in s:
14                s=s+ch
15        for i in range(len(x)):
16            if x[i] in s and y[i] in s:
17                count=count+1
18        return(count)
19