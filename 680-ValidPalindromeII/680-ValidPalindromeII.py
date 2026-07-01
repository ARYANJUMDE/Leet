# Last updated: 7/1/2026, 2:47:47 PM
1class Solution(object):
2    def countSubstrings(self, s):
3        x=[]
4        for i in range(len(s)):
5            for j in range(i+1,len(s)+1):
6                if s[i:j]==s[i:j][::-1]:
7                    x.append(s[i:j])
8        return(len(x))
9        