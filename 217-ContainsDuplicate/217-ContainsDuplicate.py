# Last updated: 7/2/2026, 1:16:58 PM
1class Solution(object):
2    def isIsomorphic(self, s, t):
3        hashmap1={}
4        hashmap2={}
5        for i in range(len(s)):
6            if s[i] in hashmap1:
7                if hashmap1[s[i]]!=t[i]:
8                    return(False)
9            else:
10                hashmap1[s[i]]=t[i]
11            if t[i] in hashmap2:
12                if hashmap2[t[i]]!=s[i]:
13                    return(False)
14            else:
15                hashmap2[t[i]]=s[i]
16        return(True)
17
18
19        