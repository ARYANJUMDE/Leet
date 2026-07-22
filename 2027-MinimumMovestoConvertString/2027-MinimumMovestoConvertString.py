# Last updated: 7/22/2026, 6:26:13 PM
1class Solution(object):
2    def minimumMoves(self, s):
3        count=0
4        if "X" in s:
5            while "X" in s:
6                for i in range(0,len(s)):
7                    if s[i]=="X":
8                        s=s[:i]+"000"+s[i+3:]
9                        count=count+1
10                        break
11            return(count)
12        else:
13            return(0)
14
15        