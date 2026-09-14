# Last updated: 9/14/2026, 5:42:46 PM
1class Solution(object):
2    def minWindow(self, s, t):
3        # map1={}
4        # min_len=float('inf')
5        # start=-1
6        # if len(t)>len(s):
7        #     return("")
8        # else:
9        #     for i in range(len(t)):
10        #         if t[i] not in map1:
11        #             map1[t[i]]=1
12        #         else:
13        #             map1[t[i]]=map1[t[i]]+1
14        #     k=map1.copy()
15        #     for i in range(len(s)):
16        #         k=map1.copy()
17        #         count=0
18        #         for j in range(i,len(s)):
19        #             if s[j] in map1 and k[s[j]]>0:
20        #                 count=count+1
21        #                 k[s[j]]=k[s[j]]-1
22        #             if count==len(t):
23        #                 if j-i<min_len:
24        #                     min_len=j-i
25        #                     start=i
26        #                 break
27        #     if (start==-1):
28        #         return("")
29        #     else:
30        #         return(s[start:(start+min_len+1)])
31
32        map1={}
33        min_len=float('inf')
34        start=-1
35        l=0
36        r=0
37        count=0
38        if len(t)>len(s):
39            return ""
40        else:
41            for i in range(len(t)):
42                if t[i] not in map1:
43                    map1[t[i]]=1
44                else:
45                    map1[t[i]]=map1[t[i]]+1
46            k=map1.copy()
47            while r<len(s):
48                if s[r] in map1:
49                    k[s[r]]=k[s[r]]-1
50                    if k[s[r]]>=0:
51                        count=count+1
52                while count==len(t):
53                    if r-l+1<min_len:
54                        min_len=r-l+1
55                        start=l
56                    if s[l] in map1:
57                        k[s[l]]=k[s[l]]+1
58                        if k[s[l]]>0:
59                            count=count-1
60                    l=l+1
61                r=r+1
62        if start==-1:
63            return ""
64        else:
65            return (s[start:(start+min_len)])
66