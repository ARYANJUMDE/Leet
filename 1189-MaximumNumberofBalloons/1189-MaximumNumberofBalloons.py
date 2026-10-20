# Last updated: 10/20/2026, 6:56:20 PM
1class Solution(object):
2    def maxNumberOfBalloons(self, text):
3        p="balloon"
4        t={}
5        for ch in text:
6            if ch in  p:
7                if ch not in t:
8                    t[ch]=1
9                else:
10                    t[ch]=t[ch]+1
11        count=0
12        o=True
13        while o:
14            for ch in p:
15                if ch in t:
16                    if t[ch]!=0:
17                        t[ch]=t[ch]-1
18                    else:
19                        o=False
20                        break
21                else:
22                    o=False
23                    break
24                if ch=='n':
25                    count=count+1
26        return(count)
27