# Last updated: 6/30/2026, 8:36:23 PM
1class Solution(object):
2    def frequencySort(self, s):
3        # from collections import Counter
4        # freq=Counter(s)
5        # p=sorted(s,key=lambda x:(freq[x],x),reverse=True)
6        # return(''.join(p))
7        t=""
8        x=[]
9        for ch in s:
10            if ch not in t:
11                t=t+ch
12        for i in range(len(t)):
13            x.append([t[i],s.count(t[i])])
14        x=sorted(x,key=lambda x:x[1],reverse=True)
15        r=""
16        for i in range(len(x)):
17            r=r+x[i][0]*x[i][1]
18        return(r)
19