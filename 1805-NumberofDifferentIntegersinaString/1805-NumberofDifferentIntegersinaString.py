# Last updated: 7/3/2026, 4:47:48 PM
1class Solution(object):
2    def numDifferentIntegers(self, word):
3        x=[]
4        t=[]
5        for i in range(97,123):
6            x.append(chr(i))
7        for i in range(len(word)):
8            if word[i] in x:
9                word=word.replace(word[i]," ")
10        i=0
11        while i<(len(word)):
12            if word[i]!=" ":
13                p=word[i]
14                j=i
15                for j in range(i+1,len(word)):  
16                    if word[j]!=" ":
17                        p=p+word[j]
18                    else:
19                        if int(p) not in t:
20                            t.append(int(p))
21                        break
22                else:
23                    if int(p) not in t:
24                        t.append(int(p))
25                i=j+1
26            else:
27                i=i+1
28        return(len(t))
29
30    
31        