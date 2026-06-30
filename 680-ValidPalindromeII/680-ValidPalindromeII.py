# Last updated: 6/30/2026, 9:27:53 PM
1class Solution(object):
2    def mergeAlternately(self, word1, word2):
3        t=""
4        v=""
5        z=abs(len(word1)-len(word2))
6        if z!=0:
7            if min(len(word1),len(word2))==len(word1):
8                for i in range(z):
9                    word1=word1+" "
10            else:
11                for i in range(z):
12                    word2=word2+" "
13        for i in range(len(word1)):
14            t=t+word1[i]
15            t=t+word2[i]
16        for i in range(len(t)):
17            if t[i]!=" ":
18                v=v+t[i]
19        return(v)
20
21        