# Last updated: 7/16/2026, 8:49:35 PM
1class Solution(object):
2    def commonChars(self, words):
3        t=words[0]
4        z=""
5        x=[]
6        for ch in t:
7            if ch not in z:
8                z=z+ch
9        for i in range(len(z)):
10            p=[]
11            for j in range(len(words)):
12                p.append(words[j].count(z[i]))
13            if min(p)>0:
14                x.extend((z[i]*min(p)))
15        return(x)
16
17        