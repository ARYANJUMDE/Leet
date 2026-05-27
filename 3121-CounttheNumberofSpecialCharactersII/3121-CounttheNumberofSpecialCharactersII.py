# Last updated: 5/27/2026, 11:04:19 AM
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
11        for ch in word:
12            if ch not in s:
13                s=s+ch
14        for i in range(len(x)):
15            if (x[i] in s and y[i] in s) and (word.rindex(x[i])<word.index(y[i])):
16                count=count+1
17        
18        return(count)
19            
20
21        
22        